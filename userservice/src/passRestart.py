from sqlalchemy.exc import SQLAlchemyError
from tableModel import *

class RestartPasswordCode():
    def __init__(self):
        pass

    def updateCode(self, mail: str, db) -> dict:
        pass
        
    def update(self, password: str, db) -> dict:
        """ ## Update
            ## Upisivanje korisnika u bazu
            - ``password``
                - db == FastAPI(Session=Depends(get_db))
                ##### osluskuje i otvara seassi-u

            ### Koristi User klasu, poziva atribute i dodeljuje vrednosti.
        """
        
        Base = User()
        
        # kreiranje tabele svaki put kada se pozove User - create table if table does not exist:
        Base.metadata.create_all(bind=engine)

        try:
          
            # update pass
            data = User(
                password=password
            )
            
            db.add(data)

            db.commit()
            db.refresh(data)


            data

        except SQLAlchemyError as e:
            #hvata exception ako pokusa da se upise korisnik sa istim emailom jer je polje unique
            return {"postgresError": e, "error": True}

        return {"PasswordUpdate": password, "tableName": data.__tablename__, "error": False}
