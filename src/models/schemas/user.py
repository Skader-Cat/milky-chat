from typing import Optional

from pydantic import BaseModel
from uuid import UUID

class UserResponse(BaseModel):
    id: UUID
    email: str
    username: str
    avatar: Optional[str]
    role: str

class UserResponseSmall(BaseModel):
    id: UUID
    username: str
    avatar: Optional[str]

class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    avatar: Optional[str]

class UserUpdate(BaseModel):
    username: Optional[str]
    password: Optional[str]
    avatar: Optional[str]

class UserFull(BaseModel):
    id: UUID
    username: str
    password: str
    email: str
    role: str
    avatar: Optional[str]

class UserListResponse(BaseModel):
    users: list[UserResponse]
    total: int
    page: int
    size: int




