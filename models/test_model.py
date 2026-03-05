from sqlalchemy import Column, Integer, String
from database.db import Base


class Test(Base):
    __tablename__ = "test"
    message = Column(String, nullable=False,primary_key=True)
