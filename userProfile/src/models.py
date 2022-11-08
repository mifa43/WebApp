from typing import Dict, List, Optional

from pydantic import BaseModel


class UserProfile(BaseModel):
    keycloakUserID: str

class Token(BaseModel):
    file: bytes = None
    token: str

class UpdateUserProfile(BaseModel):
    UserFirstName: str
    UserLastName: str
    UserNumber: str
    token: str

    title: str
    description: str
    about: str
    tagInput: str
    links: str
    firstStepsComplete: bool