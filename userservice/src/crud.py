from click import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from tableModel import User

class Postgres():
    def __init__(self):
        self.engine = engine = create_engine(
            "postgresql+psycopg2://mifa43:koliko43@user-service-postgres-dev/userservice",
            isolation_level="SERIALIZABLE", echo=True
        )
        self.db = db = scoped_session(sessionmaker(bind=self.engine))
        self.base = Base = declarative_base()

    def createTable(self):
        table1 = User().registerTable()
        
        return {"func": table1}

    def insertUser(self):
        data = User().insert("Mifa43","Kotez", "some@.com", 121312312, "123445")
        return {"insert": data}
