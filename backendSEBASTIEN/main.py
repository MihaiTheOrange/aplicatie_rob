from fastapi import FastAPI, Depends, APIRouter
from pydantic import BaseModel, conlist
from datetime import datetime
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Optional, List

models.Base.metadata.create_all(bind=engine)


class Senzor1(BaseModel):
    inp: Optional[int] = None


def deschide():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI()

sen1_router = APIRouter(
    prefix='/sen1',
    tags=['senzorul_1']
)


@sen1_router.get('/get', operation_id="sen1data")
def get_data_query(db: Session = Depends(deschide)):
    data = db.query(models.Senzor1).all()
    return data


@sen1_router.post('/post', operation_id="sen1post")
def create_log(log: Senzor1, db: Session = Depends(deschide)):
    log_model = models.Senzor1()
    log_model.inp = log.inp
    db.add(log_model)
    db.commit()
    return {'message': f'succes added input:{id}'}


app.include_router(sen1_router)


comenzi_router = APIRouter(
    prefix='/comenzi',
    tags=['comenzi']
)


class Com(BaseModel):
    comenzi: List[int]
    rgb: List[int]


clist = [Com(comenzi=[0,0,0,0], rgb=[0,0,0])]


@comenzi_router.post('/post')
def post_command(comanda: Com):
    clist.insert(0, comanda)
    clist.pop()
    return clist


@comenzi_router.get('/get')
def get_command():
    return ''.join(map(str, clist[0].comenzi))+' '+' '.join(map(str, clist[0].rgb))


app.include_router(comenzi_router)
