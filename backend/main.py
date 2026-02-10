from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import models
from .database import get_db ,engine
import math, random

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/dtest')
def test():
    return{"Status":'Success'}
