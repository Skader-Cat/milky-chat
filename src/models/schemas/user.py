import enum
import uuid
from enum import Enum, auto

from pydantic import BaseModel

class EnumMixin:
    pass

class UserFull(BaseModel, EnumMixin):
    id: uuid.UUID
    username: str
    email: str
    tag: str
    avatar: str
    channels: list[str]
    messages: list[str]
    class Config:
        orm_mode = True

    def __getattr__(self, item):
        return item