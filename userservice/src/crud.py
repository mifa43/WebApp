from click import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from tableModel import User
import os

class Postgres():
    def __init__(self):
        self.engine = create_engine(
                    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}",
                    isolation_level="SERIALIZABLE", echo=True)
        self.Base = declarative_base()
        self.Base = User()
        self.Base.metadata.create_all(bind=self.engine)
        
    def insert(self, name: str, lastName: str, mail: str, phoneNumber: str, password: str) -> dict:
        """ ## Insert
            ## Upisivanje korisnika u bazu
            - ``name``
            - ``lastName``
            - ``mail``
            - ``phoneNumber``
            - ``password``

            ### Koristi User klasu, poziva atribute i dodeljuje vrednosti.
        """
        try:
            Seassion = sessionmaker(bind=self.engine)
            seassion = Seassion()

            #Dodeljivanje vrednosti
            user = User()
            user.name = name
            user.lastName = lastName
            user.mail = mail
            user.phoneNumber = phoneNumber
            user.password = password

            #Izvrsavanje 
            seassion.add(user)
            seassion.commit()

            #Zatvaranje seassi-e
            seassion.close()
        except SQLAlchemyError as e:
            #hvata exception ako pokusa da se upise korisnik sa istim emailom jer je polje unique
            return {"postgresError": e, "error": True}

        return {"UserInserted": name, "tableName": User.__tablename__, "error": False}
