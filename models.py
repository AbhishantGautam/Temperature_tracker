from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean, Float
from database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import null, text

class Post(Base): #creating a table for sql alchemy using Base parent class for inheritance
    __tablename__ = "mytable"

    datetime = Column(TIMESTAMP, primary_key=True, nullable=False)
    temp = Column(Float, nullable=False)
    feelslike = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    precip = Column(Float, nullable=False)
    windspeed = Column(Float, nullable=False)
    winddir = Column(Float, nullable=False)
    sealevelpressure = Column(Float, nullable=False)
    visibility = Column(Float, nullable=False)
    pred_temp = Column(Float, nullable=False)
