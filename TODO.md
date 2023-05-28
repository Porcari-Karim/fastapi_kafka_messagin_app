## FastApi app:  
[x] Create a "User" model to do data validation and to help data storage  
[x] Connect to mongodb and be able to store pydantic models as json in mongodb  
[x] Build an authentication/auhtorization system app indipendant by storing a JWT in an http-only cookie  
[x] Create fastapi dependencies to make the routes depends on it  
[ ] Create a "admin_topic_created" topic to wich each instance of the app should be listening for to be aware of when a topic is created and add it to the topic list  
[ ] Find a solution to store only one Consumer + Producer per topic in the app and not one Producer + Consumer per Websocket connection.  
[ ] Create an MVP using only two http routes "Index" containing all the rooms and being able to create rooms, the "room/<room_name>" route to be able to read and write chats to a specific room. The last route is a ws (websockets) route to make the chat app realtime using kafka to be able to share the same rooms acroos multiples instances of the same fastapi app.  