import asyncio
import re

from decoraters import *


@PasswordIsEqualToPassword
def checkPassword(password1, password2):
    """### Pomocna funkcija

       #### Pre izvrsavanja funkcije dekorater uzima argumente, \
        proverava da li su pass1 i pass2 isti i vraca u funkciju
    
        - :`password1`
        - :`password2`
    """
    return password1