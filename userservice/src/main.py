from fastapi import FastAPI, HTTPException, Depends
import logging, uvicorn
from crud import Postgres
from models import *
from sqlalchemy.orm import Session
from database import get_db
from passRestart import RestartPasswordCode
from fastapi_cprofile.profiler import CProfileMiddleware

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

# app.add_middleware(CProfileMiddleware, enable=True, print_each_request = True, strip_dirs = False, sort_by='cumulative', filename='/tmp/output.pstats', server_app = app)


# @app.get("/gettest")
# async def get_by_id(id:int,db:Session=Depends(get_db)):
#     return db.query(User).filter(User.id == id).first()

@app.get("/")
def helth_check():

    logger.info("{Health : OK}, 200")
    
    return {"Health": "OK"}

@app.post("/insert-user")
def insert_user(model: UserModel, db:Session=Depends(get_db)):
    """Hvatanje requesta i slanje u insert funkciju"""
    try:
        data = Postgres().insert(model.UserName, model.UserFirstName, model.UserLastName, model.UserEmail, model.UserNumber, model.UserPassword, db)     # hvataj request body

        if data["error"] == False:  # postgres je uspesno upisao u bazu

            logger.info({"InsertUser": data["UserInserted"], "tableName": data["tableName"]})

            return {"InsertUser": data["UserInserted"], "tableName": data["tableName"]}
    except:

        logger.error(data["postgresError"])

        raise HTTPException(status_code = 409, detail = "failed")

    if data["error"] == True:   # postgres je podigao gresku

        logger.error(data["postgresError"])

        raise HTTPException(status_code = 409, detail = "Username or email already exists")

    else:   # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")

@app.post("/password-restart")
def password_restart(model: RestartPasswordModel, db:Session=Depends(get_db)):

    userCodeUpdate = RestartPasswordCode().updateCode(model.UserEmail, model.code, db)

    logger.info({"codeUpdate": userCodeUpdate["code"], "tableName": userCodeUpdate["tableName"]})

    return {"codeUpdate": userCodeUpdate["code"], "tableName": userCodeUpdate["tableName"]}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")