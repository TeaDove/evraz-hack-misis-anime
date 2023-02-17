from dataclasses import dataclass

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

    def get_all_events(self):
        return self.collection_event.find_one()

    def insert_event(self, event: ExhausterEvent):
        try:
            self.collection_event.insert_one(event.jsonable_dict())
        except DuplicateKeyError:
            logger.exception("duplicated.key", exc_info=True)
