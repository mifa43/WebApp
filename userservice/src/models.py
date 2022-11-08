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
    imageURL: str
    keycloakUserID: str

class UpdateUserProfile(BaseModel):
    firstName: str
    lastName: str
    phoneNumber: str
    keycloakUserID: str
    title: str
    description: str
    about: str
    tagInput: str
    links: str
    firstStepsComplete: bool
# class RestartPasswordModel(BaseModel):
#     UserEmail: str
#     code: str