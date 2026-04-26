from database.db import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

class UserTypes(Base):
    __tablename__ = "user_types"
    id = Column(String, nullable=False,primary_key=True) 
    name = Column(String)

class Users(Base):
    __tablename__ = "users"
    id = Column(String, nullable=False,primary_key=True)
    email = Column(String,nullable=True)
    password_hash = Column(String)
    username = Column(String)
    user_type_id = relationship("user_types")
    created_at = DateTime()
    updated_at = DateTime()

class Sessions(Base):
    __tablename__ = "sessions"
    id = Column(String, nullable=False,primary_key=True)
    userID = relationship("users")
    session_token = Column(String)
    expires_at = Column(DateTime)
    created_at = Column(DateTime)

