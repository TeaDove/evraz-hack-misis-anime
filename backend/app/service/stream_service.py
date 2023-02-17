import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from tqdm import tqdm

import pandas as pd
from schemas.exhauster import ExhausterEvent
from service.mapping_service import MappingService


@dataclass
class StreamService:
    mapping_service: MappingService

    def process_record(self, record: Dict[str, Any]) -> None:
        for idx in range(self.mapping_service.exhauster_count):
            exhauster_event = ExhausterEvent(
                created_at=record.get("moment"), exhauster_id=idx
            )
            self.mapping_service.map_signals(exhauster_event, record)

    def store_records_localy(self, record: Dict[str, Any]) -> None:
        events = []
        for idx in range(self.mapping_service.exhauster_count):
            exhauster_event = ExhausterEvent(
                created_at=record.get("moment"), exhauster_id=idx
            )
            self.mapping_service.map_signals(exhauster_event, record)
            events.append(exhauster_event.dict())

        pd.json_normalize(events).to_csv(f"data/kafka_records/{uuid.uuid4()}.csv")

    def concat_local_records(self) -> None:
        df = pd.DataFrame()
        for file in tqdm(Path("data/kafka_records/").iterdir()):
            if file.name == ".gitkeep":
                continue

            df = pd.concat([df, pd.read_csv(file)])

        df.to_csv(f"data/kafka_records_concat/{datetime.utcnow().isoformat()}.csv")
