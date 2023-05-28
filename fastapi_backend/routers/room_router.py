from fastapi import APIRouter, Response, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates

from broker_connection.kafka_connection import listen_to_channel, create_channel_producer, get_only_rooms_topics, get_all_topics

templates = Jinja2Templates(directory="templates")

room_router = APIRouter(prefix="/room")

@room_router.get("/{id}")
async def get_room(id: int, request: Request) -> Response:

    return templates.TemplateResponse("room.html", {"request": request})

@room_router.websocket("/ws/{anme}")
async def websocket_endpoint(name: str, request: Request, websocket: WebSocket):
    await websocket.accept()
    consumer = await listen_to_channel(name)
    producer = await create_channel_producer(name)
    async def consume_kafka_messages():
        for message in consumer:
            str_message = message.value.decode()
            await websocket.send(name, str_message)
    consume_kafka_messages()
    try:
        while True:
            message = await websocket.receive_text()
            producer.send(name, message.encode())
    except WebSocketDisconnect:
        return

@room_router.post("/create")
async def room_index(name: str):
    if name not in await get_all_topics():
        producer = await create_channel_producer("admin_topic")
        producer.send("admin_topic", name.encode())


    return {}

@room_router.get("/")
async def get_all_rooms():
    return await get_only_rooms_topics()