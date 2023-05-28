import asyncio
from kafka import KafkaConsumer
from kafka_utils.config import bootstrap_servers
from kafka_utils.kafka_admin import create_new_topic

def listen() -> None:
    consumer = KafkaConsumer("admin_topic", bootstrap_servers=bootstrap_servers)
    for message in consumer:
        str_message = message.value.decode()
        print(f"Trying to create new topic {str_message}")
        create_new_topic(str_message)

if __name__ == "__main__":
    listen()
