from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from .database import engine,sesion_local
import schemas,models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#
# @app.get("/")
def index():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}
