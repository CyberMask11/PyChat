from sqlalchemy import Column, String, Integer
import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import base

class Users(base):
    __tablename__ = "Users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    displayname = Column(String(120), unique=True)
    username = Column(String(120), unique=True)
    password = Column(String(250))