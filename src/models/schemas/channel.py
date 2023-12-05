import uuid

from pydantic import BaseModel

class ChannelSmall(BaseModel):
    id: uuid.UUID
    owner_id: str
    class Config:
        orm_mode = True

class ChannelMedium(BaseModel):
    id: uuid.UUID
    name: str
    owner_id: str
    description: str
    class Config:
        orm_mode = True

class ChannelLarge(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    users: list[str]
    avatar: str
    class Config:
        orm_mode = True