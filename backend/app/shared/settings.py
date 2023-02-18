import multiprocessing as mp

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    kafka_host: str
    kafka_topic: str
    kafka_user: str
    kafka_password: str
    kafka_ca_pem_path: str = "CA.pem"
    kafka_consumer_group: str = "misisAnimeBoys"
    kafka_read_from_start: bool = True

    mongo_database: str = "evraz"
    mongo_host: str = "localhost"
    mongo_port: int = 27017
    mongo_username: str = "root"
    mongo_password: str = "root"

    uvicorn_host: str = "localhost"
    uvicorn_port: int = 8000
    uvicorn_workers: int = mp.cpu_count() * 2
    uvicorn_log_level: str = "WARNING"

    class Config:
        env_prefix = "misis_"
        env_file = ".env"


app_settings = AppSettings()
