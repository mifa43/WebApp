from pydantic import BaseModel
from typing import List, Optional

class RegisterForm(BaseModel):
    UserName: str
    UserLastName: str
    UserPassword: str
    # UserNumber: int
    UserEmal: str
    # Terms: bool