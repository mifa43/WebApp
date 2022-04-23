from pydantic import BaseModel
from typing import List, Optional

class RegisterForm(BaseModel):
    UserName: str
    UserLastName: str
    UserNumber: int
    UserEmal: str
    Terms: bool

#                 <input type="text" class="UserName" id="UserName" placeholder="Your username">
#                 <input type="text" class="UserLastName" id="UserLastName" placeholder="Your lastname">
#                 <input type="number" class="UserNumber" id="UserNumber" placeholder="Your phone number">
#                 <input type="email" class="UserEmal" id="UserEmail" placeholder="Your email">