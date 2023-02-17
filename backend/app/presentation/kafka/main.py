import ssl
from concurrent.futures import ThreadPoolExecutor

import orjson

from kafka import KafkaConsumer, TopicPartition
from presentation.dependencies import container
from shared.base import logger
from shared.settings import app_settings


def _process_record_safe(record):
    try:
        container.stream_service.process_record(orjson.loads(record.value))
    except Exception:
        logger.exception("internal.server.error")


def _set_consumer() -> KafkaConsumer:
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    consumer = KafkaConsumer(
        bootstrap_servers=app_settings.kafka_host,
        security_protocol="SASL_SSL",
        sasl_mechanism="SCRAM-SHA-512",
        group_id=app_settings.kafka_consumer_group,
        ssl_context=context,
        sasl_plain_username=app_settings.kafka_user,
        sasl_plain_password=app_settings.kafka_password,
        # auto_offset_reset="oldest",
    )
    topic = app_settings.kafka_topic
    partitions = consumer.partitions_for_topic(topic)
    topic_partitions = tuple(
        TopicPartition(topic, partition) for partition in partitions
    )
    consumer.assign(topic_partitions)
    consumer.seek_to_beginning(*topic_partitions)
    return consumer


def listen_kafka() -> None:
    consumer = _set_consumer()
    executor = ThreadPoolExecutor()

    for idx, record in enumerate(consumer):
        logger.debug(f"start.processing.record.{idx}")
        executor.submit(_process_record_safe, record)
        if idx > 1:
            break


def listen_kafka_store_localy() -> None:
    consumer = _set_consumer()

    for idx, record in enumerate(consumer):
        logger.debug(f"start.processing.record.{idx}")
        container.stream_service.store_records_localy(orjson.loads(record.value))
