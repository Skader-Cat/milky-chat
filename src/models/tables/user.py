import datetime
import uuid

from sqlalchemy import Column, UUID, String, DateTime
from sqlalchemy.orm import Relationship

from db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    role = Column(String)
    password = Column(String)
    avatar = Column(String)
    chats = Relationship("Chat", secondary="user_chat", back_populates="users")
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())