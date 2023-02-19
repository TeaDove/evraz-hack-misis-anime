from pydantic import BaseSettings

from kafka import KafkaConsumer


class Settings(BaseSettings):
    kafka_host: str
    kafka_topic: str
    kafka_user: str
    kafka_password: str

    class Config:
        env_file = ".env"
        env_prefix = "misis_"


settings = Settings()


def get_kafka_connect() -> KafkaConsumer:
    consumer = KafkaConsumer(
        bootstrap_servers=settings.kafka_host,
        security_protocol="SASL_SSL",
        sasl_mechanism="SCRAM-SHA-512",
        group_id="misis_anime",
        enable_auto_commit=False,
        sasl_plain_username=settings.kafka_user,
        sasl_plain_password=settings.kafka_password,
        ssl_cafile="./CA.pem",
    )
    return consumer


get_kafka_connect()
