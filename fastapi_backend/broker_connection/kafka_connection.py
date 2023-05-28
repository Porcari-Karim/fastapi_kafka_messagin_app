from kafka import KafkaConsumer, KafkaProducer, KafkaAdminClient
from .config import bootstrap_servers

async def listen_to_channel(channel_name: str) -> KafkaConsumer:
    return KafkaConsumer(channel_name, bootstrap_servers=bootstrap_servers)

async def create_channel_producer(channel_name: str) -> KafkaProducer:
    return KafkaProducer(bootstrap_servers=bootstrap_servers)

async def get_all_topics() -> list[str]:
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    topic_partitions = admin_client.list_topics()

    topic_names = [topic for topic in topic_partitions]

    
    return topic_names

async def get_only_rooms_topics() -> list[str]:
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    topic_partitions = admin_client.list_topics()

    topic_names = [topic for topic in topic_partitions]

    topic_names.remove("admin_delete_topic")
    topic_names.remove("admin_topic")
    
    return topic_names
