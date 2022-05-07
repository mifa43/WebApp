from pydoc import doc
from typing import AsyncContextManager
from fastapi import FastAPI, HTTPException
import logging, uvicorn
from crud import Postgres
from models import *
# kreiranje logera https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__) 
logger.setLevel("DEBUG")

# kreiranje logger consol
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# format
formatter = logging.Formatter('%(levelname)s:     %(name)s.%(funcName)s: %(message)s')

# dodaj format u consol-u
ch.setFormatter(formatter)

# dodaj consol-u logger
logger.addHandler(ch)

app = FastAPI()

@app.get("/")
async def helth_check():

    logger.info("{Health : OK}, 200")
    
    return {"Health": "OK"}

@app.post("/insert-user")
async def insert_user(model: UserModel):
    """Hvatanje requesta i slanje u insert funkciju"""
    
    data = Postgres().insert(model.UserName, model.UserLastName, model.UserEmail, model.UserNumber, model.UserPassword)     # hvataj request body
    
    if data["error"] == False:  # postgres je uspesno upisao u bazu

        logger.info({"InsertUser": data["UserInserted"], "tableName": data["tableName"]})

        return {"InsertUser": data["UserInserted"], "tableName": data["tableName"]}

    if data["error"] == True:   # postgres je podigao gresku

        logger.error(data["postgresError"])

        raise HTTPException(status_code = 409, detail = "Username or email already exists")

    else:   # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")
        
if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")