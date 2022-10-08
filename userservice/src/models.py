from pydantic import BaseModel
from typing import List, Optional

# model za hvatanje requesta i slanje u insert funkciju

class UserModel(BaseModel):
    UserName: str
    UserFirstName: str
    UserLastName: str
    UserEmail: str
    UserNumber: str
    keycloakUserID: str

# class RestartPasswordModel(BaseModel):
#     UserEmail: str
#     code: str