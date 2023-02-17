from dataclasses import dataclass

from repository.mongo_repository import MongoRepository
from service.mapping_service import MappingService
from service.stream_service import StreamService


@dataclass
class Container:
    stream_service: StreamService


def init_combat_container() -> Container:
    mapping_service = MappingService()

    mongo_repository = MongoRepository()
    stream_service = StreamService(
        mapping_service=mapping_service, mongo_repository=mongo_repository
    )
    return Container(stream_service=stream_service)
