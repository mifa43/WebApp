from pydantic import BaseModel
from typing import List, Optional

class UserModel(BaseModel):
    UserName: str
    UserLastName: str
    UserEmail: str
    UserNumber: str
    UserPassword: str