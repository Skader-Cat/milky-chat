import uuid
from enum import Enum

from pydantic import BaseModel

from models.schemas.user import UserFull, FieldCollectorMixin


class UserAuth(UserFull):
    class Register(BaseModel):
        username: str
        email: str
        password: str
        id: uuid.UUID

    class Login(BaseModel):
        username: str
        password: str