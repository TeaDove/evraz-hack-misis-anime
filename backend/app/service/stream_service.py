import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from tqdm import tqdm

import pandas as pd
from repository.mongo_repository import MongoRepository
from schemas.exhauster import ExhausterEvent
from service.mapping_service import MappingService
from shared.base import logger


@dataclass
class StreamService:
    mapping_service: MappingService
    mongo_repository: MongoRepository

    def process_record(self, record: Dict[str, Any]) -> None:
        for idx in range(self.mapping_service.exhauster_count):
            exhauster_event = ExhausterEvent(
                created_at=record.get("moment"), exhauster_id=idx
            )
            self.mapping_service.map_signals(exhauster_event, record)
            self.mongo_repository.insert_event(exhauster_event, record)

    def dump_from_db(self) -> None:
        events = []
        for event in tqdm(self.mongo_repository.get_all_events()):
            events.append(event)

        folder = Path("data/kafka_records_concat")
        folder.mkdir(exist_ok=True)

        pd.json_normalize(events).to_parquet(
            folder / f"{datetime.utcnow().strftime('%Y-%m-%dT%H:%M')}.pqt"
        )

    def store_records_localy(self, record: Dict[str, Any]) -> None:
        events = []
        for idx in range(self.mapping_service.exhauster_count):
            exhauster_event = ExhausterEvent(
                created_at=record.get("moment"), exhauster_id=idx
            )
            self.mapping_service.map_signals(exhauster_event, record)
            events.append(exhauster_event.dict())

        folder = Path("data/kafka_records")
        folder.mkdir(exist_ok=True)

        pd.json_normalize(events).to_parquet(folder / f"{uuid.uuid4()}.pqt")

    def concat_local_records(self) -> None:
        df = pd.DataFrame()
        for file in tqdm(Path("data/kafka_records/").iterdir()):
            if file.name == ".gitkeep":
                continue
            try:
                df = pd.concat([df, pd.read_parquet(file)])
            except Exception:
                logger.exception("concat.error")

        folder = Path("data/kafka_records_concat")
        folder.mkdir(exist_ok=True)

        df.to_parquet(folder / f"{datetime.utcnow().strftime('%Y-%m-%dT%H:%M')}.pqt")
