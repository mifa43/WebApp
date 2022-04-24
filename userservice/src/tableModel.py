from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine(
                    "postgresql+psycopg2://mifa43:koliko43@user-service-postgres-dev/userservice",
                    isolation_level="SERIALIZABLE", echo=True
                )
class User(Base):
    """Model tabele"""
    __tablename__= "registration"   #ime tabele
     
    #kolone u tabeli i njihove karakteristike
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("username", String)
    lastName = Column("lastname",String)
    mail = Column("mail",String)
    phoneNumber = Column("phonenumber", Integer)
    password = Column("password",String)

    def registerTable(self):

        """Fukcija uzima model i genersi sql upit i kreira tabelu"""

        Base.metadata.create_all(bind=engine)

        return {"TableName": "Table created"}

    def insert(self):
        """Upisivanje korisnika u bazu 
        Koristi User klasu, poziva atribute i dodeljuje vrednosti
        """
        Seassion = sessionmaker(bind=engine)
        seassion = Seassion()

        user = User()
        user.name = "milos"
        user.lastName = "milos"
        user.mail = "milos"
        user.phoneNumber = 132313
        user.password = "milos"


        seassion.add(user)
        seassion.commit()
        print("user inserted")
        seassion.close()
        return {"TableName": "User inserted"}