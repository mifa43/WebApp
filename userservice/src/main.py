import logging

import uvicorn
from crud import Postgres, asyncio
from database import get_db
from fastapi import Depends, FastAPI, HTTPException
# from passRestart import RestartPasswordCode
from fastapi_cprofile.profiler import CProfileMiddleware
from models import *
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from tableModel import User
from helpers import modelToDict

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

@app.get("/")
def helth_check():
    """ ### Ovo je test endpoint i koristi se samo za testiranje 
        `{Health : OK}`
    """

    logger.info("{Health : OK}, 200")
    
    return {"Health": "OK"}

@app.get("/get-user")
async def get_user(keycloakUserID: str, db: Session=Depends(get_db)):
    """ ### Vrati korisnika za dati ID
        
        - `keycloakUserID`: unique=True
    """
    try:    # pokusavamo da izvvrsimo query ako nece dizem sql error

        query = db.query(User).filter(User.keycloakUserID == keycloakUserID).first()    # trazimo korisnika za dati keycloakID 
        
        if query == None:   # ako je Query None znaci da nema vrednosti za dati ID

            logger.error({f"404: The user with given ID was not founded or does not exist"})

            raise HTTPException(status_code = 404, detail = "The user with given ID was not founded or does not exist")
        
        elif query:  # ako smo dobili tip podatka str znaci da je korisnik pronadjen u bazi
            
            logger.error({"200": "User founded"})

            return {"query": query, "status": True}   # dbException smo dodali kako bi izbegli keyError
        
        else:   # desilo se nesto neocekivano

            logger.error({"500": "Something went wrong"})

            raise HTTPException(status_code = 500, detail = "Something went wrong")
        
    except SQLAlchemyError as e:    # ako se digne exception znaci da baza nije pronadjena ili se desilo nesto neockivano zato vracamo e

        logger.error({"dbException": "Database or table does not exist"})
        
        raise HTTPException(status_code = 500, detail = "Database or table does not exist")
        # return {"dbException": True, "reason": e}   # vracamo dbException ako imamo problem sa bazom

@app.post("/insert-user")
async def insert_user(model: UserModel, db:Session=Depends(get_db)):
    """ ### Hvatanje requesta i slanje u insert funkciju
        - `UserModel`: Ocekivani request body    
    """
    try:

        data = await asyncio.create_task(Postgres().insert(
                model.UserEmail, 
                model.keycloakUserID, 
                db
                ))     # hvataj request body

        if data["error"] == False:  # postgres je uspesno upisao u bazu

            logger.info({"InsertUser": data["UserInserted"], "tableName": data["tableName"]})

            return {"InsertUser": data["UserInserted"], "tableName": data["tableName"]}
    except:

        logger.error(data["postgresError"])

        raise HTTPException(status_code = 409, detail = "failed")

    if data["error"] == True:   # postgres je podigao gresku

        logger.error(data["postgresError"])

        raise HTTPException(status_code = 409, detail = "Username or email already exists")

    else:   # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")

@app.post("/update-user-image")
async def update_user_image(model: UpdateImage, db:Session=Depends(get_db)):
    """ ### Ovaj endpoint upisuje url slike koje je vratio Cloudinary 
        - `model.imageUrl`: source image url 
        - `model.keycloakUserID`: keycloak id iz baze
    """
    
    dic = modelToDict(model)

    update = Postgres().update(dic, model.keycloakUserID, db)

    if update["error"] == False:    # try blok je izvrsen bez problema 

        if update["update"] == 1:   # ako je update: 1 znaci da je uspesno updejtovan korisnik

            logger.info(update)
        
            return {"update": "OK", "detail": False} # response oke
        
        else:   # ako je update: 0 znaci da koriosnik nije updejtovan

            logger.error({"404": "The user with given ID was not founded or does not exist"})

            raise HTTPException(status_code = 404, detail = "The user with given ID was not founded or does not exist")

    elif update["error"] == True:   # podignut SQLAlchemy exception; vracamo error: ture

        logger.error({"404": "Database or table does not exist"})

        raise HTTPException(status_code = 404, detail = "Database or table does not exist")

    else:   # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")

@app.put("/update-user-profile")
def update_user_profile(model: UpdateUserProfile, db:Session=Depends(get_db)):
    """ ### Update user profile endpoint
        #### **Polja za update su opociona**
        - `model.UserFirstName`
        - `model.UserLastName`
        - `model.UserEmail`
        - `model.UserNumber`
        - `model.keycloakUserID`
    """

    dic = modelToDict(model)

    update = Postgres().update(dic, model.keycloakUserID, db)

    if update["error"] == False:    # try blok je izvrsen bez problema 

        if update["update"] == 1:   # ako je update: 1 znaci da je uspesno updejtovan korisnik

            logger.info(update)
        
            return {"update": "OK", "detail": False} # response oke
        
        else:   # ako je update: 0 znaci da koriosnik nije updejtovan

            logger.error({"404": "The user with given ID was not founded or does not exist"})

            raise HTTPException(status_code = 404, detail = "The user with given ID was not founded or does not exist")

    elif update["error"] == True:   # podignut SQLAlchemy exception; vracamo error: ture

        logger.error({"404": "Database or table does not exist"})

        raise HTTPException(status_code = 404, detail = "Database or table does not exist")

    else:   # desilo se nesto neocekivano

        logger.error({"500": "Something went wrong"})

        raise HTTPException(status_code = 500, detail = "Something went wrong")

if __name__ == "__main__":

    uvicorn.run(app, port=8080, loop="asyncio")

# @app.post("/password-restart")
# def password_restart(model: RestartPasswordModel, db:Session=Depends(get_db)):

#     userCodeUpdate = RestartPasswordCode().updateCode(model.UserEmail, model.code, db)  # email koristimo kao id i izvlacimo id i trazimo u relaciji owner_id updejtamo code polje

#     logger.info({"codeUpdate": userCodeUpdate["codeUpdated"], "tableName": userCodeUpdate["tableName"]})

#     return {"codeUpdate": userCodeUpdate["codeUpdated"], "tableName": userCodeUpdate["tableName"]}


#su - postgres && psql -U mifa43 userservice

