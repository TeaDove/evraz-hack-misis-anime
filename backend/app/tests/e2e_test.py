from shared.containers import init_combat_container
from tests.record import record

container = init_combat_container()


class TestClass:
    def test_process_record(self):
        container.stream_service.process_record(record)
