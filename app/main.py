from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
# from .schemas import 
from .models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

#
@app.get("/")
def index():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}
