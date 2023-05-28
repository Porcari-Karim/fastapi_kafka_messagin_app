import sys
from kafka import KafkaProducer
from kafka_utils.config import bootstrap_servers

def produce_once(topic_name: str, message: bytes) -> None:
    producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
    producer.send(topic_name, message.encode())
    producer.flush()


if __name__ == "__main__":
    produce_once(*sys.argv[1:])