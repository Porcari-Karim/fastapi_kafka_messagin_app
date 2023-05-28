from pydantic import BaseModel

class JWTPayload(BaseModel):
    id: str
    username: str