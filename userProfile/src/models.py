from typing import Dict, List, Optional

from pydantic import BaseModel


class UserProfile(BaseModel):
    keycloakUserID: str

class Token(BaseModel):
    file: bytes = None
    token: str

class UpdateUserProfile(BaseModel):
    UserFirstName: Optional[str] = None
    UserLastName: Optional[str] = None
    UserNumber: Optional[str] = None
    token: str

    title: Optional[str] = None
    description: Optional[str] = None
    about: Optional[str] = None
    tagInput: Optional[List] = None
    links: Optional[str] = None
    firstStepsComplete: Optional[bool] = None