from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaConsumer
from kafka.errors import UnknownTopicOrPartitionError
from .config import bootstrap_servers

def create_new_topic(topic_name: str, num_partitions: int = 1, replication_factor: int = 1) -> None:
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    # Créer un nouveau topic
    new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
    admin_client.create_topics([new_topic])

    # Vérifier que le topic a été créé
    topic_metadata = admin_client.list_topics()
    print(topic_metadata)

    # Fermer la connexion admin
    admin_client.close()

def delete_existing_topic(topic_name: str) -> None:
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    try:
        admin_client.delete_topics([topic_name])
        print(f"Le topic '{topic_name}' a été supprimé avec succès.")
    except UnknownTopicOrPartitionError:
        print(f"Le topic '{topic_name}' n'existe pas.")

    # Vérifier que le topic a été créé
    topic_metadata = admin_client.list_topics()
    print(topic_metadata)

    # Fermer la connexion admin
    admin_client.close()

def check_active_consumers(topic, admin_client = None):
    # Create a KafkaAdminClient instance
    if admin_client is None:
        admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    # Get the list of consumer group IDs
    consumer_groups = admin_client.list_consumer_groups()

    # Check for active consumers in each consumer group
    for group_id in consumer_groups:
        consumer = KafkaConsumer(group_id=group_id, bootstrap_servers=bootstrap_servers)
        topics = consumer.subscription()

        # If the topic is subscribed by any consumer group, return True
        if topic in topics:
            return True

    # If no active consumers found for the topic
    return False

def get_topic_creation_timestamp(topic_name, admin_client = None):
    # Create a KafkaAdminClient instance
    if admin_client is None:
        admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    # Retrieve metadata for the specified topic
    topic_metadata = admin_client.describe_topics(topic_name)

    # Extract the creation timestamp from the topic metadata
    creation_timestamp = topic_metadata[topic_name].creation_timestamp / 1000  # Convert milliseconds to seconds

    return creation_timestamp


def get_only_rooms_topics(admin_client=None) -> list[str]:
    if admin_client is None:
        admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

    topic_partitions = admin_client.list_topics()

    topic_names = [topic for topic in topic_partitions]

    topic_names.remove("admin_delete_topic")
    topic_names.remove("admin_topic")
    
    return topic_names