import uuid

from pydantic import BaseModel

class UserBase(BaseModel):
    tag: str
    username: str
    password: str
    email: str

class UserFull(UserBase):
    id: uuid.UUID
    avatar: str
    channels: list[str]
    messages: list[str]

    class Config:
        from_attributes = True