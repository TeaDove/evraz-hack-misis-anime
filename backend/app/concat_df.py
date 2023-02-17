from shared.containers import init_combat_container

container = init_combat_container()
if __name__ == "__main__":
    container.stream_service.concat_local_records()
