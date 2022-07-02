from fastapi import FastAPI, HTTPException, BackgroundTasks
import logging, uvicorn
from fastapi.middleware.cors import CORSMiddleware
from auth_methods import KeycloakAuth
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
async def helth_check():

    logger.info("{Health : OK}, 200")

    return {"Health": "OK"}

@app.post("/login")
async def login(model: AuthCreaditional):

    if model.UserEmail and model.UserPassword:  # da li postoji input ? da 

        try: # pokusaj login

            auth = KeycloakAuth().login(model.UserEmail, model.UserPassword)    # login

            logger.info("accessToken: ",auth)

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

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")