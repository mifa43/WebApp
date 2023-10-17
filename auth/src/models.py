from typing import List, Optional

from pydantic import BaseModel

# model za fastapi post metodu koja hvata requestove

class AuthCreaditional(BaseModel):
    UserEmail: str
    UserPassword: str

class RefreshToken(BaseModel):
    token: str



class UserPasswordRestart(BaseModel):
    UserEmail: str

    
    # code: Optional[str] = None
    

# class RestartPassword(UserPasswordRestart):
#     password1: Optional[str] = None
#     password2: Optional[str] = None