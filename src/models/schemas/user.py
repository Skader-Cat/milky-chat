import enum
import uuid
from enum import Enum, auto
from typing import Any, Dict, Optional

import pydantic.v1
from pydantic import BaseModel, create_model, Field

from models.schemas import FieldCollectorMixin, ChannelLarge
from models.tables import Channel


class UserFull(BaseModel, FieldCollectorMixin):
    id: uuid.UUID
    username: str
    email: str
    tag: str
    avatar: str
    channels: list[ChannelLarge]
    messages: list[str]
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

#TODO: исправить наследование для UserAuth