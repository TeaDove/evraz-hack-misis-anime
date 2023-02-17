from kafka import KafkaConsumer
from shared.settings import app_settings


def listen_kafka() -> None:
    KafkaConsumer(
        bootstrap_servers=app_settings.kafka_host,
        security_protocol="SASL_SSL",
        sasl_mechanism="SCRAM-SHA-512",
        group_id=app_settings.kafka_consumer_group,
        enable_auto_commit=False,
        sasl_plain_username=app_settings.kafka_user,
        sasl_plain_password=app_settings.kafka_password,
        ssl_cafile=app_settings.kafka_ca_pem_path,
    )
