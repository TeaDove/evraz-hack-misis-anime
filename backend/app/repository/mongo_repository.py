from dataclasses import dataclass
from typing import Any, Dict, Iterable

from pydantic import ValidationError

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from schemas.exhauster import ExhausterEvent
from shared.base import logger
from shared.settings import app_settings


@dataclass
class MongoRepository:
    def __post_init__(self):
        self.client = MongoClient(
            host=app_settings.mongo_host,
            port=app_settings.mongo_port,
            username=app_settings.mongo_username,
            password=app_settings.mongo_password,
        )
        self.database = self.client.get_database("test")
        self.collection_event = self.database.get_collection("event")

    def get_all_events(self) -> Iterable[ExhausterEvent]:
        curs = self.collection_event.find()
        for document in curs:
            try:
                yield ExhausterEvent.parse_obj(document)
            except ValidationError:
                logger.exception("document.validation.error")

    def insert_event(self, event: ExhausterEvent, record: Dict[str, Any]):
        try:
            self.collection_event.insert_one(
                dict(
                    original_record=record,
                    **event.jsonable_dict(),
                )
            )
        except DuplicateKeyError:
            logger.exception("duplicated.key", exc_info=True)
