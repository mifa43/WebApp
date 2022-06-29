from pydantic import BaseModel
from typing import List, Optional

# model za fastapi post metodu koja hvata requestove

class RegisterForm(BaseModel):
    UserName: str
    UserLastName: str
    UserEmail: str
    UserNumber: str
    UserPassword: str
    UserRePassword: str
    
class Verification(BaseModel):
    UserName: str