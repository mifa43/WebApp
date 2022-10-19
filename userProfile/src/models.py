from typing import Dict, List, Optional

from pydantic import BaseModel


class UserProfile(BaseModel):
    keycloakUserID: str

class Token(BaseModel):
    file: bytes = None
    token: str