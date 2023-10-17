from typing import List, Optional

from pydantic import BaseModel

# model za hvatanje requesta i slanje u insert funkciju

class UserModel(BaseModel):
    UserEmail: str
    keycloakUserID: str

class UpdateImage(BaseModel):
    imageURL: str
    keycloakUserID: str

class UpdateUserProfile(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    phoneNumber: Optional[str] = None
    keycloakUserID: str
    title: Optional[str] = None
    description: Optional[str] = None
    about: Optional[str] = None
    tagInput: Optional[List] = None
    links: Optional[str] = None
    firstStepsComplete: Optional[bool] = None
# class RestartPasswordModel(BaseModel):
#     UserEmail: str
#     code: str
