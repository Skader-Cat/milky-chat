from pydantic import BaseModel
from sqlalchemy import UUID

from models.schemas import UserMedium, UserSmall


class ChannelSmall(BaseModel):
    id: UUID
    owner_id: [UserSmall]
    class Config:
        orm_mode = True

class ChannelMedium(BaseModel):
    id: UUID
    name: str
    owner_id: [UserMedium]
    description: str
    class Config:
        orm_mode = True

class ChannelLarge(BaseModel):
    id: UUID
    name: str
    description: str
    users: list[UserMedium]
    avatar: str
    class Config:
        orm_mode = True