from pydantic import BaseModel
from typing import List, Optional

# model za hvatanje requesta i slanje u insert funkciju

class UserModel(BaseModel):
    UserName: str
    UserLastName: str
    UserEmail: str
    UserNumber: str
    UserPassword: str