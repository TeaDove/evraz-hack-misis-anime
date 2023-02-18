from dataclasses import dataclass
from typing import Iterable, List

from repository.mongo_repository import MongoRepository, SortOrders
from schemas.event import ExhausterEvent
from schemas.exhauster import Exhauster
from shared.base import logger


@dataclass
class ExhausterService:
    mongo_repository: MongoRepository

    def __post_init__(self):
        self.exhausters_stubs: List[Exhauster] = [
            Exhauster(
                exhauster_id=0,
                name="Эксгаустер № 1 (У-171)",
                machine_name="Агломашина № 1",
            ),
            Exhauster(
                exhauster_id=1,
                name="Эксгаустер № 2 (У-172)",
                machine_name="Агломашина № 1",
            ),
            Exhauster(
                exhauster_id=2,
                name="Эксгаустер № 3 (Ф-171)",
                machine_name="Агломашина № 2",
            ),
            Exhauster(
                exhauster_id=3,
                name="Эксгаустер № 4 (Ф-172)",
                machine_name="Агломашина № 2",
            ),
            Exhauster(
                exhauster_id=4,
                name="Эксгаустер № 5 (X-171)",
                machine_name="Агломашина № 3",
            ),
            Exhauster(
                exhauster_id=5,
                name="Эксгаустер № 6 (X-172)",
                machine_name="Агломашина № 3",
            ),
        ]

    def get_events_by_exhauster(
        self, exhauster_id: int, sort_order: SortOrders, page: int, size: int
    ) -> Iterable[ExhausterEvent]:
        return self.mongo_repository.get_events_by_exhauster(
            exhauster_id=exhauster_id, sort_order=sort_order, page=page, size=size
        )

    def get_exhausters(self) -> Iterable[Exhauster]:
        return self.mongo_repository.get_exhausters()

    def update_exhauster(self, event: ExhausterEvent) -> None:
        exhauster = self.mongo_repository.get_exhauster(event.exhauster_id)

        if exhauster is None:
            logger.critical("exhauster.not.found")
            return

        if exhauster.status.work.is_working != event.status.work.is_working:
            exhauster.last_replacement = event.created_at

        exhauster.status = event.status
        exhauster.last_update = event.created_at

        self.mongo_repository.update_exhauster(exhauster=exhauster)
