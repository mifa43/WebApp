from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    """Model tabele koja ce da se kreira u bazi"""
    
    __tablename__= "registration"   #ime tabele
     
    #kolone u tabeli i njihove karakteristike
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("username", String)
    lastName = Column("lastname",String)
    mail = Column("mail",String, unique=True)
    phoneNumber = Column("phonenumber", String)
    password = Column("password",String)