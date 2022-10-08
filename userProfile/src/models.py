from pydantic import BaseModel
from typing import List, Optional

class UserProfile(BaseModel):
    keycloakUserID: str