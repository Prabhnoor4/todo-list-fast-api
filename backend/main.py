from fastapi import HTTPException,FastAPI,Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, SessionLocal, Base, get_db

Base.metadata.create_all(bind=engine)

app= FastAPI()

