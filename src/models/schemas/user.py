from pydantic import BaseModel

from models.schemas.channel import ChannelMedium


class UserSmall(BaseModel):
    id: str
    class Config:
        orm_mode = True


class UserMedium(BaseModel):
    id: str
    username: str
    email: str
    class Config:
        orm_mode = True

class UserLarge(BaseModel):
    id: str
    username: str
    email: str
    tag: list
    avatar: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

class UserFull(BaseModel):
    id: str
    username: str
    email: str
    tag: list
    channels: list[ChannelMedium]
    avatar: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True