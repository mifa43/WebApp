# from sqlalchemy.exc import SQLAlchemyError
# from tableModel import *

# class RestartPasswordCode():
#     """ ### Klasa za menjanje koda i passworda
#         - `updateCode` -> upisi novi kod koji stize na korisnikov zahtev

#     """
#     def __init__(self):
#         pass

#     def updateCode(self, mail: str, code: str, db) -> dict:
#         """ ## Update
#             ## Upisivanje novi kod u bazu i updejta
#             - ``code``
#                 - db == FastAPI(Session=Depends(get_db))
#                 ##### osluskuje i otvara seassi-u

#             ### Koristi PasswordReset klasu, poziva atribute i dodeljuje vrednosti.
#         """

#         query = db.query(User).filter(User.mail == mail)    # uzmi userID *param email (select id from "table" where mail = mail)

#         userID = [row for row in query] # pretraga rezultata

#         codeUpdate = db.query(PasswordReset).filter(PasswordReset.owner_id == userID[0].id).update({'code': code})  # updejtuj code 

#         db.commit()

#         return {"codeUpdated": True, "tableName": "managePassword"}

#     def update(self, email: str , password: str, db) -> dict:
#         """ ## Update
#             ## Upisivanje password u bazu i updejta
#             - ``password``
#                 - db == FastAPI(Session=Depends(get_db))
#                 ##### osluskuje i otvara seassi-u

#             ### Koristi User klasu, poziva atribute i dodeljuje vrednosti.
#         """
        
#         Base = User()
        
#         # kreiranje tabele svaki put kada se pozove User - create table if table does not exist:
#         Base.metadata.create_all(bind=engine)

#         try:
          
#             # update pass
#             passwordUpdate = db.query(User).filter(User.password == email).update({'password': password})
            
#             db.add(passwordUpdate)

#             db.commit()
#             db.refresh(passwordUpdate)


            

#         except SQLAlchemyError as e:
#             #hvata exception ako pokusa da se upise korisnik sa istim emailom jer je polje unique
#             return {"postgresError": e, "error": True}

#         return {"PasswordUpdate": password, "tableName": User.__tablename__, "error": False}
