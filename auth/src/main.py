from fastapi import FastAPI, HTTPException, BackgroundTasks
import logging, uvicorn
from fastapi.middleware.cors import CORSMiddleware
from auth_methods import KeycloakAuth
from password_restart import KeycloakUserPasswordManage
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

origins = [
    "*",
    "http://0.0.0.0:8083/"
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
def helth_check():

    logger.info("{Health : OK}, 200")

    return {"Health": "OK"}

@app.post("/login")
def login(model: AuthCreaditional):

    if model.UserEmail and model.UserPassword:  # da li postoji input ? da 

        try: # pokusaj login

            auth = KeycloakAuth().login(model.UserEmail, model.UserPassword)    # login

            logger.info("accessToken: {0}".format(auth))

            return auth     # vrati access token

        except:  # ako nece input je pogresan ili korisnik nije registrovan

            logger.error({"406": "The creaditionals are incorrect"})

            raise HTTPException(status_code = 406, detail = "The creaditionals are incorrect")

    elif model.UserEmail and model.UserPassword == None:    # input je none dizi gresku

        logger.error({"406": "The username or password is incorrect"})

        raise HTTPException(status_code = 406, detail = "The username or password is incorrect")

    elif len(model.UserEmail) <= 0 and len(model.UserPassword) <= 0:    # input je prazan str duzine 0
    
        logger.error({"406": "The fields are empty"})   

        raise HTTPException(status_code = 406, detail = "The fields are empty") # dizi error

    else: # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")

@app.post("/logout")
def logout(model: RefreshToken):

    if model.token:
        try:

            token = KeycloakAuth().logout(model.token)
            
            logger.info("accessToken: ",token)

            return {"message" :token["KeycloakAuthLogout"]}   # vrati access token

        except:

            logger.error({"406": "The token is invalid or expired"})

            raise HTTPException(status_code = 406, detail = "The token is invalid or expired")

    elif model.token == None or model.token == "":

        logger.error({"406": "The entered value is not valid, a refsresh_token is required"})

        raise HTTPException(status_code = 406, detail = "The entered value is not valid, a refsresh_token is required")

    else: # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")

@app.post("/password-restart")
def password_restart(model: UserPasswordRestart):
    userID = KeycloakUserPasswordManage().getKeycloakUserId(model.UserEmail)

    return {"OK": "200"}

    
if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")