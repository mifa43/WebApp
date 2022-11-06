import asyncio
import datetime
import logging

import requests_async as asyncRequests
import uvicorn
from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cprofile.profiler import CProfileMiddleware
from helpers import (checkNameAndEmail, checkPassword, createUserName,
                     emailValidation)
from keycloakManager.KeycloakID import GetKeycloakID
from keycloakManager.keycloakRegister import CreateUser
from keycloakManager.sendVerification import SendVerification
from keycloakManager.keycloakUserUpdate import UpdateUser
from models import *
from requester import SendRequest
from resend_email_verfy import ResendVerifyEmail

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

# testira api endpoint preformanse i vreme izvrsavanja
# app.add_middleware(CProfileMiddleware, enable=True, print_each_request = True, strip_dirs = False, sort_by='cumulative', filename='/tmp/output.pstats', server_app = app)

origins = [
    "*",
    "http://0.0.0.0:8081/"
]
# allow cors request
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*","post"],
    allow_headers=["*"],
)


# https://fastapi.tiangolo.com/tutorial/cors/

@app.get("/")
async def helth_check():

    logger.info({"Health": "OK"})

    return {"Health": "OK"}

@app.post("/resend-email-verification")
async def resend_email_verificatioin(model: Verification):

    userID = ResendVerifyEmail().getKeycloakUserID(model.UserName)  # da li user id postoji ?

    if userID["exist"] == True: # ako postoji saljemo verifikaciju

        verify = ResendVerifyEmail().sendVerification(userID["user_id_keycloak"])   # slanje verifikacije !

        logger.info({"EmailVerificationSend": [True, model.UserName]})
        

        return {"EmailVerificationSend": [True, model.UserName]}


    elif userID["exist"] == False:  # keycloak user id nije pronadjen dizemo error

        logger.error({"406": "Keycloak userID does not exist"})

        raise HTTPException(status_code = 406, detail = "Keycloak userID does not exist")

    else: # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")


@app.post("/register-user")
# @pytest.mark.anyio
async def register_user(model: RegisterForm, background_tasks: BackgroundTasks):
    # logger.info(app.add_middleware(CProfileMiddleware, enable=True, server_app = app, filename='/tmp/output.pstats', strip_dirs = False, sort_by='cumulative'))
    """Hvatanje requesta i slanje na userservice"""

  
    email = emailValidation(model.UserEmail)    # da li je email validan ? 

    password = checkPassword(model.UserPassword, model.UserRePassword)  # da li se passwordi podudaraju ?

    lower = checkNameAndEmail(model.UserName, model.UserEmail)  # vrati email i username malim slovima !

    if email["EmailIsValid"] == True and password["passwordIsValid"] == True:   # da li su email i password validni True ?

        userName = createUserName(model.UserName, model.UserLastName)   # username je kombinacija - str ime.prezime

        # kreiraj usera na keycloak-u async
        # slnje rquesrta async
        # SendRequest.userService(userName, model.UserName ,model.UserLastName, lower["email"], model.UserNumber, password["check"])

        #user name je user emailo jer se samo prijavljujemo emailom jer je na keyclaoku username obavezan, email koristimo za social media auth
        kc = await asyncio.create_task(CreateUser(lower["email"], lower["email"], model.UserName, model.UserLastName, password["check"]).new())  # cekaj da se vrati keycloak user id


        async with asyncRequests.Session() as session:  # saljemo async Request session

            job = SendRequest.userService(lower["email"], model.UserName ,model.UserLastName, lower["email"], model.UserNumber, kc["clientID"], session)   # arguument session

            reqq = await asyncio.gather(*job["Response"]) # uzima corutine, Return a future aggregating results from the given coroutines/futures. Ovo je kao u javascriptu promise

            for resp in reqq:   # respose

                req = resp.json()

   
        if kc["kcError"] == False:  # ako korisnik koji se registruje nema nalog(*username, *email, unique true) kc error je false i saljemo verifikaciju

            logger.info("Email: Send ")

            # asyncio.create_task(CreateKeycloakUser().sendVerifyEmail(kc["clientID"]))   # async email verify
            asyncio.create_task(SendVerification(kc["clientID"]).send())   # async email verify

        handler = req  # email postoji u bazi ? 

        if "detail" in handler: # postgres dize error i vraca kao response

            logger.error({"409": "Username or email already exists in db"})

            raise HTTPException(status_code = 409, detail = "Username or email already exists in db")

        if kc["ID"] == False or kc["ID"] == None:   # korisnik nije pronadjen dizi exception i vrati response

            logger.error({"406": "UserID does not exist"})

            raise HTTPException(status_code = 406, detail = "UserID does not exist")

        elif kc["kcError"] == True:   # korisnik koji se registruje uneo je vec iskorisceni email ili username
    
            logger.error({"409": "Username or email already exists in kc"})

            raise HTTPException(status_code = 409, detail = "Username or email already exists in kc")
    
        # ako su sve unete vrednosti validne kreira se korisnik na kc i bazi i salje email verify
        

        logger.info({
            "PostRequestSendOn": [job["PostRequestSendOn"], req], 
            "keycloak": [kc["clientID"], kc["userName"]],
            "verifyEmail": kc["ID"]
            })

        return {
            "PostRequestSendOn": job["PostRequestSendOn"],
            "Response": req, 
            "keycloak": [kc["clientID"], kc["userName"]],
            "verifyEmail": kc["ID"]
            }

    elif password["passwordIsValid"] == False:  # passwordi se ne podudaraju vrati except

        logger.error({"406": "Password: Passwords do not match"})

        raise HTTPException(status_code = 406, detail = "Passwords do not match")

    elif email["EmailIsValid"] == False:    # email nije email vrati except

        logger.error({"422": "Email: Unprocessable entity"})

        raise HTTPException(status_code = 422, detail = "Email: Unprocessable entity")
        
    else:   # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")
    
@app.post("/update-user")
async def update_user(model: UpdateUserModel):

    body = {'firstName': model.UserFirstName, 'lastName': model.UserLastName}

    update = await asyncio.create_task(UpdateUser(model.keycloak_id).send(body))

    logger.info({"userUpdate": update})

    return {"userUpdate": update}

    # treba da se preuredi registracija, kao user lastname i firstname treba da se izbace sa obzirom da je username obavezan,
    # treba da se doda za username mail kako bi smo izbacili visak koda. email je jedinstven i nece se menjati
    # takodje treba da se odradi update za bazu
    # frontend: izbaciti first i last name kao i br telefona, dodati neki korak za popunjavanje nekih osnovnih informacija 

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")


# async preformanse sa 2s na 0.2 sec 