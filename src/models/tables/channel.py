from sqlalchemy import Column, String, UUID, DateTime
from sqlalchemy.orm import Relationship

from models.db import base


class Channel(base):
    __tablename__ = "channels"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    owner_id = Relationship("User", secondary="user_channels", back_populates="channels")
    messages = Relationship("Message", secondary="channel_messages", back_populates="channels")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<Channel(id={self.id}, name={self.name}, user_id={self.user_id})>"
class ChannelMessage(base):
    __tablename__ = "channel_messages"

    id = Column(UUID, primary_key=True, index=True)
    channel_id = Column(UUID)
    message_id = Column(UUID)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<ChannelMessage(id={self.id}, channel_id={self.channel_id}, message_id={self.message_id})>"