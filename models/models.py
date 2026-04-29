from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, default="user@email.com")
    role = Column(String, default="staff")

    points = Column(Integer, default=0)
    steps = Column(Integer, default=0)
    mood = Column(Integer, default=0)

    challenges_completed = Column(Integer, default=0)