from pydantic import BaseModel
from typing import List, Dict, Optional

class UserProfile(BaseModel):
    keycloakUserID: str

class Token(BaseModel):
    file: bytes = None
    token: str