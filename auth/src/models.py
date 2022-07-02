from pydantic import BaseModel
from typing import List, Optional

# model za fastapi post metodu koja hvata requestove

class AuthCreaditional(BaseModel):
    UserEmail: str
    UserPassword: str
