from sqlalchemy import Column, UUID, DateTime, String

from models.db import base


class Message(base):
    __tablename__ = "messages"

    id = Column(UUID, primary_key=True, index=True)
    content = Column(String)
    user_id = Column(UUID)
    channel_id = Column(UUID)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<Message(id={self.id}, content={self.content}, user_id={self.user_id}, channel_id={self.channel_id})>"