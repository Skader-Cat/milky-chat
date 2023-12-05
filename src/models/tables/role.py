from sqlalchemy import Column, String, DateTime, UUID
from sqlalchemy.orm import Relationship

from models.db import base


class Role(base):
    __tablename__ = "roles"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<Role(id={self.id}, name={self.name}, user_id={self.user_id})>"


class UserRole(base):
    __tablename__ = "user_roles"

    id = Column(UUID, primary_key=True, index=True)
    user_id = Column(UUID)
    role_id = Column(UUID)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<UserRole(id={self.id}, user_id={self.user_id}, role_id={self.role_id})>"