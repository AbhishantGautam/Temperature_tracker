# from os import stat
# from typing import Optional, List
from datetime import datetime
from fastapi import FastAPI, Response, status, HTTPException, Depends, Request
# from fastapi.params import Body
# from pydantic import BaseModel
# import random
# import psycopg2
# from starlette.status import HTTP_404_NOT_FOUND
# from psycopg2.extras import RealDictCursor
# import time
# from . import models
import pathlib
from models import Post
from database import get_db
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
import pathlib
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent

templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

# Base.metadata.create_all(bind=engine)

app = FastAPI()

datetime_list = []
temp_list = []
feelslike_list = []
humidity_list = []
precip_list = []
windspeed_list = []
winddir_list = []
sealevelpressure_list = []
visibilty_list = []
pred_temp_list = []

@app.get("/", response_class=HTMLResponse)
async def root(request: Request, db: Session = Depends(get_db)):
    user = db.query(Post).all()
    print(len(user))
    if not datetime_list:
        for item in range(0,len(user)-1):
            datetime_list.append(user[item].datetime)
            temp_list.append(user[item].temp)
            feelslike_list.append(user[item].feelslike)
            humidity_list.append(user[item].humidity)
            precip_list.append(user[item].precip)
            windspeed_list.append(user[item].windspeed)
            winddir_list.append(user[item].winddir)
            sealevelpressure_list.append(user[item].sealevelpressure)
            visibilty_list.append(user[item].visibility)
            pred_temp_list.append(user[item].pred_temp)

    elif user[len(user)-1].datetime not in datetime_list:
        datetime_list.append(user[len(user)-1].datetime)
        temp_list.append(user[len(user)-1].temp)
        feelslike_list.append(user[len(user)-1].feelslike)
        humidity_list.append(user[len(user)-1].humidity)
        precip_list.append(user[len(user)-1].precip)
        windspeed_list.append(user[len(user)-1].windspeed)
        winddir_list.append(user[len(user)-1].winddir)
        sealevelpressure_list.append(user[len(user)-1].sealevelpressure)
        visibilty_list.append(user[len(user)-1].visibility)
        pred_temp_list.append(user[len(user)-1].pred_temp)

        
    dict1 = {
        'datetime' : datetime_list,
        'temp' : temp_list,
        'feelslike' : feelslike_list,
        'humidity' : humidity_list,
        'precipitation' : precip_list,
        'wind_speed' : windspeed_list,
        'wind_direction' : winddir_list,
        'pressure' : sealevelpressure_list,
        'visibilty' : visibilty_list,
        'predicted_temperature' : pred_temp_list
    }
    list1 = range(len(dict1['datetime']), len(dict1['datetime'])-30,  -1)
    return templates.TemplateResponse("index.html", {"request":request, "dict1":dict1, "list1":list1})
