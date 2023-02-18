from dataclasses import dataclass
from typing import Iterable

from repository.mongo_repository import MongoRepository, SortOrders
from schemas.exhauster import ExhausterEvent


@dataclass
class ExhausterService:
    mongo_repository: MongoRepository

    def get_events_by_exhauster(
        self, exhauster_id: int, sort_order: SortOrders, page: int, size: int
    ) -> Iterable[ExhausterEvent]:
        return self.mongo_repository.get_events_by_exhauster(
            exhauster_id=exhauster_id, sort_order=sort_order, page=page, size=size
        )
