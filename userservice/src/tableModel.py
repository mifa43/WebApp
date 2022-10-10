from sqlalchemy import Integer, String, ForeignKey, Column
from database import Base, engine
from sqlalchemy.orm import relationship

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
    keycloakUserID = Column("keycloakUserID", String, unique=True)
    imageURL = Column("imageURL", String)
    # password = Column("password",String)

    # managePassword = relationship("PasswordReset",cascade="all, delete-orphan", passive_deletes=True)
        # PasswordReset klasa tabele,  cascade="all, delete-orphan" ovo bi trebalo kada kazem orm drop table da obrise i relaciju
    def __str__(self):
          return self.name


# class PasswordReset(Base):

#         __tablename__= "managePassword"   #ime tabele

#         id = Column("id", Integer, primary_key=True, autoincrement=True)
#         code = Column("code",String)
#         # owner_id id od korisnika kome pripada kod, key je id iz registracije, ondelete="cascade" ako obrisemo usera iz registracije brise se i iz managePassword
#         owner_id = Column("owner_id", Integer, ForeignKey("registration.id", ondelete="cascade"))


        # owner = relationship("User", back_populates="managePassword")
         
         
# shell debug
# from tableModel import *
# Base = User()
# Base.metadata.create_all(bind=engine)