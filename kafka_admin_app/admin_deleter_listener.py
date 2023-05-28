import asyncio
from kafka import KafkaConsumer
from kafka_utils.config import bootstrap_servers
from kafka_utils.kafka_admin import delete_existing_topic

def listen_delete() -> None:
    consumer = KafkaConsumer("admin_delete_topic", bootstrap_servers=bootstrap_servers)
    for message in consumer:
        str_message = message.value.decode()
        print(f"Trying to delete topic {str_message}")
        delete_existing_topic(str_message)

if __name__ == "__main__":
    listen_delete()