from shared.containers import init_combat_container
from tests.record import record

container = init_combat_container()


class TestClass:
    def test_process_record(self):
        container.stream_service.process_record(record)

    def test_mongo_connect(self):
        container.stream_service.mongo_repository.get_all_events()

    def test_create_exhausters(self):
        exhausters_stubs = container.exhauster_service.exhausters_stubs
        for exhauster in exhausters_stubs:
            container.exhauster_service.mongo_repository.create_exhauster(
                exhauster=exhauster
            )
