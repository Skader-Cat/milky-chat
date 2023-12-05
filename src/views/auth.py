import uuid
from pydantic import BaseModel

class UserAuth:
    class Register(BaseModel):
        username: str
        password: str
        email: str

    class Login(BaseModel):
        email: str
        password: str

    class Update(BaseModel):
        username: str
        password: str
        email: str
        avatar: str
        channels: list[str]
        messages: list[str]

    class Delete(BaseModel):
        username: str
        password: str
        email: str
        avatar: str

    class Get(BaseModel):
        id: uuid.UUID
        username: str
        email: str
        tag: str

    class Custom:
        pass