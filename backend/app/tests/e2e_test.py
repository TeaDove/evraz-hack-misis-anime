from shared.containers import init_combat_container
from tests.record import record

container = init_combat_container()


class TestClass:
    def test_process_record(self):
        container.stream_service.process_record(record)

    def test_mongo_connect(self):
        container.stream_service.mongo_repository.get_all_events()
