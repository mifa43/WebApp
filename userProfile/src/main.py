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

    if token:   # da li token dosao do api-endpointa ? 

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

        if "detail" not in req and req["status"] == True:   # ako se u response objektu nenalazi detail i status je True nema greske i korisnik je nadjen

            logger.info({"200": "User founded"})

            return {"data": req}
                
        elif req["detail"] == "Database or table does not exist":  # ako je dbException True baza je digla problem

            logger.error({"404": "Database or table does not exist"})

            raise HTTPException(status_code = 404, detail = "Database or table does not exist")  # Vracamo FE-u 404 
        
        elif req["detail"] == "The user with given ID was not founded or does not exist": # ako u respounsu vraca detail ciljani api nije pronasao korisnika u bazi 

            logger.error({"404": "User does not exist"})

            raise HTTPException(status_code = 404, detail = "User does not exist")  # Vracamo FE-u 404 

    elif token == None: # token nema vrednost ili je none, dizemo 404

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

    keycloakUserID = TokenData(token).decode()

    urlForCheckUser = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/get-user'    # provera da li korisnik sa ID postoji pre upload-a

    payload = {
            "keycloakUserID" : keycloakUserID
            }
        # asinhrono slanje requesta, kreiramo sessino
    async with asyncRequests.Session() as session:  # saljemo async Request session

        # saljemo parametre i dobijamo corutine
        job = SendRequest(urlForCheckUser, session).get(payload)   # arguument session

        reqq = await asyncio.gather(*job["Response"]) # uzima corutine, Return a future aggregating results from the given coroutines/futures. Ovo je kao u javascriptu promise

        for resp in reqq:   # respose

            req = resp.json()

    if "detail" not in req and req["status"] == True: # ako se u response objektu nenalazi detail i status je True nema greske i korisnik je nadjen
    
        urlForUpdate = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/update-user-image'  # endpoint za upload image

        # endpoint je podesen da postuje slike na coludinary
        data = ImageDatabase(file).uploadIMG()

        # token se dekoduje i vraca userID
        
        payload = {
            "imageURL" : data["secure_url"],
            "keycloakUserID" : keycloakUserID
            }
        
        # asinhrono slanje requesta, kreiramo sessino
        async with asyncRequests.Session() as session:  # saljemo async Request session

            # saljemo parametre i dobijamo corutine
            job = SendRequest(urlForUpdate, session).post(payload)   # arguument session

            reqq = await asyncio.gather(*job["Response"]) # uzima corutine, Return a future aggregating results from the given coroutines/futures. Ovo je kao u javascriptu promise

        logger.info([keycloakUserID, data["secure_url"]])

        return {"Image uploaded": [keycloakUserID, data["secure_url"]]}

    elif req["detail"] == "Database or table does not exist":    # ako je detalj jednak tekstu dizemo exceptio

        logger.error({"404": "Database or table does not exist"})

        raise HTTPException(status_code = 404, detail = "Database or table does not exist")  # Vracamo FE-u 404 

    elif req["detail"] == "The user with given ID was not founded or does not exist":   # ako je detalj jednak tekstu dizemo exceptio

        logger.error({f"""404: The user with given ID was not founded or does not exist, image uplouding was canceled"""})

        raise HTTPException(status_code = 404, detail = "The user with given ID was not founded or does not exist, image uplouding was canceled")
    
    else: # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")
    
@app.put("/update-user-profile")
async def update_user_profile(model: UpdateUserProfile):

    url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/update-user-profile'

    payload = {
        "firstName": model.UserFirstName,
        "lastName": model.UserLastName,
        "mail": model.UserEmail,
        "phoneNumber": model.UserNumber,
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