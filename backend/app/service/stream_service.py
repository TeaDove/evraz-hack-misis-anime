from dataclasses import dataclass
from typing import Any, Dict

from schemas.exhauster import ExhausterEvent
from service.mapping_service import MappingService


@dataclass
class StreamService:
    mapping_service: MappingService

    def process_record(self, record: Dict[str, Any]) -> None:
        # print(record)
        for idx in range(self.mapping_service.exhauster_count):
            exhauster_event = ExhausterEvent(
                created_at=record.get("moment"), exhauster_id=idx
            )
            self.mapping_service.map_signals(exhauster_event, record)
            print(exhauster_event.dict(exclude_none=True))  # noqa: T201

        # print(exhauster_event)
