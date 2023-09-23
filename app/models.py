from database import Base
from sqlalchemy import column,String,Integer


class USER(Base):
    __tablename__ = "user"
    id= column(Integer,primary_key=True)
    email=column(String,unique=True)
    username=column(String)
    password=column(String)
    

