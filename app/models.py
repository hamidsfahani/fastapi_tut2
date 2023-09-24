from .database import Base
from sqlalchemy import Column, String, Integer

class USER(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String)
    password = Column(String)
