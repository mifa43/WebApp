from pydoc import doc
from typing import AsyncContextManager
from fastapi import FastAPI, HTTPException
import logging, uvicorn
from crud import Postgres
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

@app.get("/")
async def helth_check():
    logger.info("{Health : OK}, 200")
    return {"Health": "OK"}

@app.get("/insert-user")
async def insert_user():
    var = Postgres().createTable()
    dat = Postgres().insertUser()
    logger.info("{Insert user : OK}, 200")
    return {"Insert user": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")