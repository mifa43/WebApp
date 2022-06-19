from sqlalchemy import Integer, String, ForeignKey, Column
from database import Base, engine

class User(Base):
    """Model tabele koja ce da se kreira u bazi"""
    
    __tablename__= "registration"   #ime tabele
     
    #kolone u tabeli i njihove karakteristike
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("username", String, unique=True)
    firstName = Column("firstname", String)
    lastName = Column("lastname",String)
    mail = Column("mail",String, unique=True)
    phoneNumber = Column("phonenumber", String)
    password = Column("password",String)

