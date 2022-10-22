import asyncio
import logging

import os
import json
import requests_async as asyncRequests
import uvicorn
from cloudinaryDB import ImageDatabase
from fastapi import FastAPI, File, Form, Header, HTTPException, UploadFile, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cprofile.profiler import CProfileMiddleware
from models import *
from requester import SendRequest
from tokenEncode import TokenData

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


origins = [
    "*",
    "http://0.0.0.0:8081/",
    "http://0.0.0.0:8080/",
    "http://0.0.0.0:8085/"

]
# allow cors request
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*","post"],
    allow_headers=["*"],
)

@app.get("/")
async def helth_check():
    logger.info("{Health : OK}, 200")

    return {"Health": "OK"}

@app.get("/get-user-profile")
async def get_user_profile(token: str = None):
    if token:

        # putanja do user servisa
        url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/get-user'

        # funkcija uzima token te ga dekoduje i vraca keycloak id 
        keycloakUserID = TokenData(token).decode()

        # body saljemo keycloak id
        payload = {
            "keycloakUserID" : keycloakUserID
        }

        async with asyncRequests.Session() as session:  # saljemo async Request session

            job = SendRequest(url, session).get(payload)   # arguument session

            reqq = await asyncio.gather(*job["Response"]) # uzima corutine, Return a future aggregating results from the given coroutines/futures. Ovo je kao u javascriptu promise

            for resp in reqq:   # respose

                req = resp.json()

        if "detail" in req:

            logger.error({"404": "User does not exist"})

            raise HTTPException(status_code = 404, detail = "User does not exist")

        else:
            logger.info({"200": "User founded"})

            return {"data": req}
    
    elif token == None: # desilo se nesto neocekivano

        logger.error({"404": "token not founded"})

        raise HTTPException(status_code = 404, detail = "Token not founded")
    else: # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")

@app.post("/user-profile-image/")
async def user_profile_image(file: bytes = File(...), token: str = Header(default=None)):
    # kako uploudati file i dobiti token
    #1. file mora da bude byte jer ga i js pretvarau byte i salje kao forms data
    #2. importovanje Header-a i setup za prihvatanje header-a u endpointu token: str = Header(default=None))

    url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/update-user-image'


    # endpoint je podesen da postuje slike na coludinary
    data = ImageDatabase(file).uploadIMG()

    # token se dekoduje i vraca userID
    keycloakUserID = TokenData(token).decode()

    payload = {
        "imageUrl" : data["secure_url"],
        "keycloakUserID" : keycloakUserID
        }
    
    # asinhrono slanje requesta, kreiramo sessino
    async with asyncRequests.Session() as session:  # saljemo async Request session

        # saljemo parametre i dobijamo corutine
        job = SendRequest(url, session).post(payload)   # arguument session

        reqq = await asyncio.gather(*job["Response"]) # uzima corutine, Return a future aggregating results from the given coroutines/futures. Ovo je kao u javascriptu promise

    logger.info([keycloakUserID, data["secure_url"]])

    return {"Image uploaded": [keycloakUserID, data["secure_url"]]}

@app.put("/update-user-profile")
async def update_user_profile(model: UpdateUserProfile):

    url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/update-user-profile'

    payload = {
        "UserFirstName": model.UserFirstName,
        "UserLastName": model.UserLastName,
        "UserEmail": model.UserEmail,
        "UserNumber": model.UserNumber,
        "keycloakUserID": model.keycloakUserID
    }

    async with asyncRequests.Session() as session:  # saljemo async Request session 

        # saljemo parametre i dobijamo corutine
        # updejtujemo samo odredjena polja 
        job = SendRequest(url, session).put(payload)   # arguument session

        reqq = await asyncio.gather(*job["Response"]) # uzima corutine, Return a future aggregating results from the given coroutines/futures. Ovo je kao u javascriptu promise
        
        for resp in reqq:   # respose

            req = resp.json()
         
    logger.info("{Health : OK}, 200")

    return {"Health": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")