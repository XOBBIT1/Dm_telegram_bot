from pydantic import BaseModel


class BaseUserSchema(BaseModel):
    name: str
    username: str
    chat_id: int
    user_status: str
