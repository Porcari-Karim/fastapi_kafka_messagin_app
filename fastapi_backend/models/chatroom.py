from pydantic import BaseModel, Field
from .chatmessage import ChatMessage


class ChatRoom(BaseModel):
    id: str | None
    users_name_list: list[str]
    chat_messages: list[ChatMessage]