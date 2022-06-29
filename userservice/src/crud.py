from sqlalchemy.exc import SQLAlchemyError
from tableModel import *

class Postgres():
    def __init__(self):
        pass
        
    def insert(self,userName: str, name: str, lastName: str, mail: str, phoneNumber: str, password: str, db) -> dict:
        """ ## Insert
            ## Upisivanje korisnika u bazu
            - ``name``
            - ``lastName``
            - ``mail``
            - ``phoneNumber``
            - ``password``
            - ``db``
                - db == FastAPI(Session=Depends(get_db))
                ##### osluskuje i otvara seassi-u

            ### Koristi User klasu, poziva atribute i dodeljuje vrednosti.
        """
        
        Base = User()
        # kreiranje tabele svaki put kada se pozove User - create table if table does not exist:
        Base.metadata.create_all(bind=engine)

        try:
            # kreiranje korisnika
            data = User(
                name=userName,
                firstName=name,
                lastName=lastName,
                mail=mail,
                phoneNumber=phoneNumber,
                password=password
            )
            db.add(data)

            db.commit()
            db.refresh(data)

        except SQLAlchemyError as e:
            #hvata exception ako pokusa da se upise korisnik sa istim emailom jer je polje unique
            return {"postgresError": e, "error": True}

        return {"UserInserted": name, "tableName": data.__tablename__, "error": False}
