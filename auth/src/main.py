import asyncio
from operator import mod
from fastapi import FastAPI, HTTPException, BackgroundTasks
import logging, uvicorn
from fastapi.middleware.cors import CORSMiddleware
from auth_methods import KeycloakAuth
from password_restart import KeycloakUserPasswordManage
from models import *
from fastapi_cprofile.profiler import CProfileMiddleware
from helpers import *
from codeGen import recoveryCodeGenerator
from sendCodeEmail import EmailToSend
from send_request_code import CreateCodeUserService
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
async def login(model: AuthCreaditional):

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
async def logout(model: RefreshToken):

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
async def password_restart(model: RestartPassword):

    userID = KeycloakUserPasswordManage().getKeycloakUserId(model.UserEmail)    # dohavti KeycloakID ako postoji 

    if userID["exist"] == True: # user email postoji ?

        code = recoveryCodeGenerator()  # generisi kod 

        sendCode = EmailToSend(model.UserEmail, code).send()    # uzmi email i kod posalji na email adresu korisnika

        sendCodeUserservice = CreateCodeUserService(model.UserEmail, code).sendCode()  # posalji kod i email na userservice

        logger.info({
            "sendCodeUserservice": [sendCodeUserservice["PostRequestSendOn"], sendCodeUserservice["response"]]
            })
        # while model.password1 == str and model.password2 == str:
        # passwordCheck = checkPassword(model.password1, model.password2)
        
        # if passwordCheck["passwordMustBeSent"] == False:
        #     logger.error({"401 ": "Password not provided"})
        #     raise HTTPException(status_code = 401 , detail = "Password not provided")

        # if passwordCheck["passwordMustBeSent"] == True:
        #     logger.info(passwordCheck)

        # logger.info({"status": "User founded !"})
        return {"status": "User founded !"}

    elif userID["exist"] == False:  # znaci da user email nije postojeci ? dizi exception
        
        logger.error({"406": "The entered value is not valid, a refsresh_token is required"})

        raise HTTPException(status_code = 406, detail = "Keylock user does not exist: *param: {0}".format(model.UserEmail))

    else: # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")


    restartPassword = KeycloakUserPasswordManage().restartPassword(userID["user_id_keycloak"], password.password1)

    
    
if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")