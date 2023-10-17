from typing import List, Optional

from pydantic import BaseModel

# model za fastapi post metodu koja hvata requestove

class RegisterForm(BaseModel):
    UserEmail: str
    UserPassword: str
    UserRePassword: str
    
class Verification(BaseModel):
    UserName: str

class UpdateUserModel(BaseModel):
    keycloak_id: str
    UserFirstName: str
    UserLastName: str