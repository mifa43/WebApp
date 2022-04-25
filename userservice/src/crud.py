from click import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from tableModel import User

class Postgres():
    def __init__(self):
        self.engine = create_engine(
                    "postgresql+psycopg2://mifa43:koliko43@user-service-postgres-dev/userservice",
                    isolation_level="SERIALIZABLE", echo=True)
        self.Base = declarative_base()
        self.Base = User()
        self.Base.metadata.create_all(bind=self.engine)
        
    def insert(self, name: str, lastName: str, mail: str, phoneNumber: int, password: str):
        """ ## Upisivanje korisnika u bazu
            - ``name``
            - ``lastName``
            - ``mail``
            - ``phoneNumber``
            - ``password``

        Koristi User klasu, poziva atribute i dodeljuje vrednosti. Insert
        """

        Seassion = sessionmaker(bind=self.engine)
        seassion = Seassion()
        
        user = User()
        user.name = f"{name}"
        user.lastName = f"{lastName}"
        user.mail = f"{mail}"
        user.phoneNumber = int(phoneNumber)
        user.password = f"{password}"


        seassion.add(user)
        seassion.commit()
        print("user inserted")
        seassion.close()
        return {"UserInserted": "User inserted"}
