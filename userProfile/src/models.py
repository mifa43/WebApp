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
    UserEmail: str
    UserNumber: str
    keycloakUserID: str