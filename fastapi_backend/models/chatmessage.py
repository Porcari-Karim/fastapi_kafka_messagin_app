from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    id: str | None
    sender_name: str
    message: str