from kafka_utils.kafka_admin import check_active_consumers, get_topic_creation_timestamp, get_only_rooms_topics
from kafka_utils.config import bootstrap_servers
from kafka.admin import KafkaAdminClient
from kafka import KafkaProducer
import time

def population_checker():
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
    producer = KafkaProducer(bootstrap_servers= bootstrap_servers)

    while True:
        for topic in get_only_rooms_topics(admin_client):
            if not check_active_consumers(topic, admin_client):
                if (time.time() - get_topic_creation_timestamp(topic, admin_client)) > 60:
                    producer.send("admin_delete_topic", topic)
        time.sleep(60)

if __name__ == "__main__":
    population_checker()
