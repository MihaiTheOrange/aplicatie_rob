from sqlalchemy import Column, DateTime, Integer
from database import Base


class Senzor1(Base):
    __tablename__ = "senzor_1"

    id_input=Column(Integer, primary_key=True, index=True)
    inp=Column(Integer)
