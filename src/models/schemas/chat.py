import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from models.schemas import UserResponse


class ChatRoomCreate(BaseModel):
    name: str
    tag: str
    description: str
    avatar: str
    users: list[str]

class MessageCreate(BaseModel):
    chat_id: UUID
    user_id: UUID
    text: str

class MessageResponse(BaseModel):
    id: UUID
    chat_id: UUID
    user: UserResponse
    text: str
    parent_id: Optional[UUID] | None
    created_at: datetime.datetime
    updated_at: datetime.datetime

class ChatRoomResponse(BaseModel):
    id: UUID
    name: str
    description: str
    avatar: str
    users: list[UserResponse]
    owner: UserResponse
    messages: list[MessageResponse]
    created_at: datetime.datetime
    updated_at: datetime.datetime

class ChatRoomSmallResponse(BaseModel):
    id: UUID
    name: str
    avatar: str
    created_at: datetime.datetime
    updated_at: datetime.datetime