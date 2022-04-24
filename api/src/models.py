from pydantic import BaseModel
from typing import List, Optional

class RegisterForm(BaseModel):
    UserName: str
    UserLastName: str
    UserEmail: str
    UserNumber: str
    UserPassword: str
    UserRepassword: str