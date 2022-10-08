from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import logging, uvicorn, asyncio
from models import *
import requests_async as asyncRequests
from requester import SendRequest
from tokenEncode import TokenData

from cloudinaryDB import ImageDatabase
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
    "http://0.0.0.0:8081/",
    "http://0.0.0.0:8080/"
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
async def get_user_profile(token: str):

    keycloakUserID = TokenData(token).decode()

    async with asyncRequests.Session() as session:  # saljemo async Request session

        job = SendRequest.userService(keycloakUserID, session)   # arguument session

        reqq = await asyncio.gather(*job["Response"]) # uzima corutine, Return a future aggregating results from the given coroutines/futures. Ovo je kao u javascriptu promise

        for resp in reqq:   # respose

            req = resp.json()

    logger.info(req)

    return {"data": req}

@app.post("/user-profile-image/")
async def user_profile_image(file: bytes = File(...)):
    # endpoint je podesen da postuje slike na coludinary

    data = ImageDatabase(file).uploadIMG()

    logger.info("{Health : OK}, 200")

    return {"Image uploaded": data}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")