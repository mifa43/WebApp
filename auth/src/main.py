import asyncio, logging, uvicorn
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cprofile.profiler import CProfileMiddleware
from models import *
from helpers import *
# Keycloak password manager imports
from keycloakManager.keycloakID import GetKeycloakID
from keycloakManager.keycloakRestartPassword import RestartPasswordKeycloak
# keycloak auth imports
from keycloakManager.keycloakLogin import Login
from keycloakManager.keycloakLogout import Logout

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

app.add_middleware(CProfileMiddleware, enable=True, print_each_request = True, strip_dirs = False, sort_by='cumulative', filename='/tmp/output.pstats', server_app = app)


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

            auth = await asyncio.create_task(Login(model.UserEmail, model.UserPassword).getToken())
            # auth = KeycloakAuth().login(model.UserEmail, model.UserPassword)    # login

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

            # token = KeycloakAuth().logout(model.token)
            token = await asyncio.create_task(Logout(model.token).refToken())
            logger.info("message: ",token)

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
async def password_restart(model: UserPasswordRestart):
   
    userID = await asyncio.create_task(GetKeycloakID(model.UserEmail).user())  # dohavti KeycloakID ako postoji

    logger.info(userID)

    if model.UserEmail == "" :

        logger.error({"406": "The entered value is not valid, an empty value {0}, connot be processed.".format(model.UserEmail)})

        raise HTTPException(status_code = 406, detail = "The entered value is not valid: *param: {0}".format(model.UserEmail))


    if userID["exist"] == True: # user email postoji ?

        asyncio.create_task(RestartPasswordKeycloak(userID["user_id_keycloak"][0]["id"]).user())    # salji email zahtev na email sa linkom

        return {"ok": 200}
      

    elif userID["exist"] == False:  # znaci da user email nije postojeci ? dizi exception
        
        logger.error({"406": "The entered value is not valid, a refsresh_token is required"})

        raise HTTPException(status_code = 406, detail = "Keylock user does not exist: *param: {0}".format(model.UserEmail))

    else: # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")


    # restartPassword = KeycloakUserPasswordManage().restartPassword(userID["user_id_keycloak"], password.password1)

    
    
if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")