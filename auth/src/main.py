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
    logger.info("{Health : OK}, 200")

   
    return {"Health": "OK"}
@app.post("/login")
async def login(model: AuthCreaditional):
    auth = KeycloakAuth().login(model.UserEmail, model.UserPassword)
    print(auth)

    logger.info(auth)

   
    return {"Health": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")