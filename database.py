from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = 'postgresql://vuxxchsiudjzcq:19146ad6348edfd5f209c06ad460e6abae945e20d3c132bc112fa9358d2b4b6a@ec2-54-158-247-97.compute-1.amazonaws.com:5432/dad725bctfvgr'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db(): # a function that starts a session with database and automatically closes it when not in use
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()