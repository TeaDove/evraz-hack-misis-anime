from dataclasses import dataclass

from service.mapping_service import MappingService
from service.stream_service import StreamService


@dataclass
class Container:
    stream_service: StreamService


def init_combat_container() -> Container:
    mapping_service = MappingService()
    stream_service = StreamService(mapping_service=mapping_service)
    return Container(stream_service)
