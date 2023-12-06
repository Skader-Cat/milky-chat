import uuid
from enum import Enum

from pydantic import BaseModel

from models.schemas.user import UserFull


class UserAuth(UserFull):
    class Register(BaseModel):
        username: str
        password: str
        email: str

    class Login(BaseModel):
        email: str
        password: str