from fastapi import FastAPI, HTTPException
import logging, uvicorn
from fastapi.middleware.cors import CORSMiddleware
from models import *
from requester import SendRequest
from helpers import checkNameAndEmail, emailValidation, checkPassword

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
    """Hvatanje requesta i slanje na userservice"""

    email = emailValidation(model.UserEmail)    # da li je email validan ? 

    password = checkPassword(model.UserPassword, model.UserRePassword)  # da li se passwordi podudaraju ?

    lower = checkNameAndEmail(model.UserName, model.UserEmail)  # vrati email i username malim slovima !

    if email["EmailIsValid"] == True and password["passwordIsValid"] == True:   # da li su email i password validni True ?

        req = SendRequest.userService(lower["name"], model.UserLastName, lower["email"], model.UserNumber, model.UserPassword)  # ako jesu salji request !

        handler = req["Response"]   # email postoji u bazi ? 

        if "detail" in handler: # postgres dize error i vraca kao response

            logger.error({"409": "Email already exists"})

            raise HTTPException(status_code = 409, detail = "Email already exists")

        logger.info({"PostRequestSendOn": req["PostRequestSendOn"], "Response": req["Response"]})

        return {"PostRequestSendOn": req["PostRequestSendOn"], "Response": req["Response"]}

    elif password["passwordIsValid"] == False:  # passwordi se ne podudaraju vrati except

        logger.error({"406": "Password: Passwords do not match"})

        raise HTTPException(status_code = 406, detail = "Passwords do not match")

    elif email["EmailIsValid"] == False:    # email nije email vrati except

        logger.error({"422": "Email: Unprocessable entity"})

        raise HTTPException(status_code = 422, detail = "Email: Unprocessable entity")
        
    else:   # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")
        
if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")