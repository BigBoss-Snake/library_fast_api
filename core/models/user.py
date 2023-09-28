from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from core.database import Base


class User(Base):
    __tablename__ = 'user'
    id  = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

