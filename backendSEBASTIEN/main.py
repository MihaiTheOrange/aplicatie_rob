from fastapi import FastAPI, Depends, APIRouter
from pydantic import BaseModel, conlist
from datetime import datetime
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Optional, List

models.Base.metadata.create_all(bind=engine)


class Senzor1(BaseModel):
    id: int
    inp: Optional[int] = None
    data: datetime


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


@sen1_router.get('', operation_id="sen1data")
def get_data_query(limit: int = 10, db: Session = Depends(deschide)):
    data = list(db.query(models.Senzor1).all())
    return data[:limit]


@sen1_router.post('', operation_id="sen1post")
def create_log(log: Senzor1, db: Session = Depends(deschide)):
    log_model = models.Senzor1()
    log_model.id = log.id
    log_model.inp = log.inp
    log_model.data_in = log.data
    db.add(log_model)
    db.commit()
    return {'message': f'succes added input:{id}'}


app.include_router(sen1_router)

sen2_router = APIRouter(
    prefix='/sen2',
    tags=['senzor_2']
)


@sen2_router.get('', operation_id="sen2data")
def sen2data(limit: int = 10, db: Session = Depends(deschide)):
    data = list(db.query(models.Senzor2).all())
    return data[:limit]


@sen2_router.post('', operation_id="sen2post")
def sen2post(log: Senzor1, db: Session = Depends(deschide)):
    log_model = models.Senzor2()
    log_model.id = log.id
    log_model.inp = log.inp
    log_model.data_in = log.data
    db.add(log_model)
    db.commit()
    return {'message': f'succes added input:{id}'}


app.include_router(sen2_router)

sen3_router = APIRouter(
    prefix='/sen3',
    tags=['senzor_3']
)


@sen3_router.get('', operation_id="sen3data")
def sen3data(limit: int = 10, db: Session = Depends(deschide)):
    data = list(db.query(models.Senzor3).all())
    return data[:limit]


@sen3_router.post('', operation_id="sen3post")
def sen3post(log: Senzor1, db: Session = Depends(deschide)):
    log_model = models.Senzor3()
    log_model.id = log.id
    log_model.inp = log.inp
    log_model.data_in = log.data
    db.add(log_model)
    db.commit()
    return {'message': f'succes added input:{id}'}


app.include_router(sen3_router)

comenzi_router = APIRouter(
    prefix='/comenzi',
    tags=['comenzi']
)


class Com(BaseModel):
    comenzi: List[int]
    rgb: List[int]


clist = [Com(comenzi=[0,0,0,0], rgb=[0,0,0])]


@comenzi_router.post('/')
def post_command(comanda: Com):
    clist.insert(0, comanda)
    clist.pop()
    return clist


@comenzi_router.get('/')
def get_command():
    return ''.join(map(str, clist[0].comenzi))+' '+' '.join(map(str, clist[0].rgb))


app.include_router(comenzi_router)
