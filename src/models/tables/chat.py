import datetime
import uuid

from sqlalchemy import Column, UUID, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Chat (Base):
    __tablename__ = "chats"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    tag = Column(String)
    name = Column(String)
    description = Column(String)
    owner_id = Column(UUID, ForeignKey("users.id"))
    avatar = Column(String)
    users = relationship("User", secondary="user_chat", back_populates="chats")
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())

class UserChat (Base):
    __tablename__ = "user_chat"
    user_id = Column(UUID, ForeignKey("users.id"), primary_key=True)
    chat_id = Column(UUID, ForeignKey("chats.id"), primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
