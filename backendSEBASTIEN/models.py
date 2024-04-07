from sqlalchemy import Column, DateTime, Integer
from database import Base

class Senzor1(Base):
    __tablename__="senzor_1"

    id_input=Column(Integer, primary_key=True, index=True)
    inp=Column(Integer)
    data_in=Column(DateTime)


class Senzor2(Base):
    __tablename__="senzor_2"

    id_input=Column(Integer, primary_key=True, index=True)
    inp=Column(Integer)
    data_in=Column(DateTime)


class Senzor3(Base):
    __tablename__="senzor_3"

    id_input=Column(Integer, primary_key=True, index=True)
    inp=Column(Integer)
    data_in=Column(DateTime)