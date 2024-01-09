import datetime
import uuid

from sqlalchemy import Column, ForeignKey, UUID, String, DateTime

from db import Base


class Message (Base):
    __tablename__ = "messages"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    text = Column(String)
    chat_id = Column(UUID, ForeignKey("chats.id"))
    user_id = Column(UUID, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
    parent_id = Column(UUID, ForeignKey("messages.id"), nullable=True)