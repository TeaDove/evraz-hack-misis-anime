from pydantic import BaseSettings


class AppSettings(BaseSettings):
    kafka_host: str
    kafka_topic: str
    kafka_user: str
    kafka_password: str
    kafka_ca_pem_path: str = "CA.pem"
    kafka_consumer_group: str = "misisAnimeBoys"

    class Config:
        env_prefix = "misis_"
        env_file = ".env"


app_settings = AppSettings()
