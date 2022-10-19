from typing import List, Optional

from pydantic import BaseModel

# model za hvatanje requesta i slanje u insert funkciju

class UserModel(BaseModel):
    UserName: str
    UserFirstName: str
    UserLastName: str
    UserEmail: str
    UserNumber: str
    keycloakUserID: str

class UpdateImage(BaseModel):
    imageUrl: str
    keycloakUserID: str

class UpdateUserProfile(BaseModel):
    UserFirstName: str
    UserLastName: str
    UserEmail: str
    UserNumber: str
    keycloakUserID: str
# class RestartPasswordModel(BaseModel):
#     UserEmail: str
#     code: str