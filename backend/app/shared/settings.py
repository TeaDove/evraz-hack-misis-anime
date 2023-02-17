from pydantic import BaseSettings


class AppSettings(BaseSettings):
    kafka_host: str
    kafka_topic: str
    kafka_user: str
    kafka_password: str


app_settings = AppSettings()
