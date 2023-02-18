from presentation.dependencies import container
from presentation.kafka.main import listen_kafka

if __name__ == "__main__":
    exhausters_stubs = container.exhauster_service.exhausters_stubs
    for exhauster in exhausters_stubs:
        container.exhauster_service.mongo_repository.create_exhauster(
            exhauster=exhauster
        )

    listen_kafka()
