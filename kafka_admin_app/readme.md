# Kafka Admin App

Application très simple permettant de créer des topics dont le nom à été réçu à l'aide du module kafka.admin de kafka-python.
Cette application est créée afin de de ne pas donner les droits d'administrateur à toutes les applications backend pour des raisons de sécurité.

### TO DO:
[x] Céer un fonction simple permettant de créer des topics sur mon broker Kafka. 
[x] Créer un kafka consumer écoutant sur le topic "kafka_admin", le message reçu sera le nom du topic à créer, le consumer fera ensuite appel à la première fonction pour créer le topic.  
[x] Créer un fonction qui permet de supprimer un topic.  
[x] Créer le consumer qui écoute sur le topic "admin_delete_topic" et qui appellera la fonction en recevant un message.