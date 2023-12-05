from sqlalchemy import Column, Integer, String, UUID, DateTime
from sqlalchemy.orm import Relationship

from models.db import base


class User(base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    tag = Column(String)
    messages = Relationship("Message", back_populates="user")
    channels = Relationship("Channel", back_populates="user")
    roles = Relationship("Role", back_populates="user")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


class UserChannel(base):
    __tablename__ = "user_channels"

    id = Column(UUID, primary_key=True, index=True)
    user_id = Column(UUID)
    channel_id = Column(UUID)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<UserChannel(id={self.id}, user_id={self.user_id}, channel_id={self.channel_id})>"


class UserMessages(base):
    __tablename__ = "user_messages"

    id = Column(UUID, primary_key=True, index=True)
    user_id = Column(UUID)
    message_id = Column(UUID)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<UserMessages(id={self.id}, user_id={self.user_id}, message_id={self.message_id})>"
