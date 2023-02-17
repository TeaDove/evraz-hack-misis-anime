from dataclasses import dataclass

from service.stream_service import StreamService


@dataclass
class Container:
    stream_service: StreamService


def init_combat_container() -> Container:
    stream_service = StreamService()
    return Container(stream_service)
