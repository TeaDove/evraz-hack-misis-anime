import multiprocessing as mp
from typing import Optional

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    kafka_host: str
    kafka_topic: str
    kafka_user: str
    kafka_password: str
    kafka_ca_pem_path: str = "CA.pem"
    kafka_consumer_group: str = "misisAnimeBoys"
    kafka_read_from_start: bool = False
    kafka_minus_offset: Optional[int] = None

    mongo_database: str = "evraz"
    mongo_host: str = "localhost"
    mongo_port: int = 27017
    mongo_username: str = "root"
    mongo_password: str = "root"

    pg_database: str = "db_evraz"
    pg_host: str = "localhost"
    pg_port: int = 5432
    pg_username: str = "db_evraz"
    pg_password: str = "db_evraz"

    uvicorn_host: str = "localhost"
    uvicorn_port: int = 8000
    uvicorn_workers: int = mp.cpu_count() * 2
    uvicorn_log_level: str = "WARNING"

    class Config:
        env_prefix = "misis_"
        env_file = ".env"


app_settings = AppSettings()
