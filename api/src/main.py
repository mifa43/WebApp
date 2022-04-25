from fastapi import FastAPI, HTTPException
import logging, uvicorn
from fastapi.middleware.cors import CORSMiddleware
from models import *
from requester import SendRequest
# from crud import *
# import psycopg2 
# import os
# from tableStructur import User
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

@app.post("/register-user")
async def register_user(model: RegisterForm):

    req = SendRequest.userService(model.UserName, model.UserLastName, model.UserEmail, model.UserNumber, model.UserPassword)

    logger.info({"PostRequestSendOn": req["PostRequestSendOn"], "Response": req["Response"]})

    return {"PostRequestSendOn": req["PostRequestSendOn"], "Response": req["Response"]}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")