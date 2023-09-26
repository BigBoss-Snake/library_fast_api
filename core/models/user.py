from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from core.database import Base


class User(Base):
    __tablename__ = 'user'
    id  = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    is_active = Column(String)
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
    access_token = Column(String)
    refresh_token = Column(String)

