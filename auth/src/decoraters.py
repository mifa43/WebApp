import re, random
import asyncio

class PasswordIsEqualToPassword(object):
    def __init__(self, arg):
        """### dekorater za proveru passworda
        
            - : `password1`
            - : `password2`

            #### ako je pass1 jedank pass2 vracamo `passwordIsValid`: `True`

        """
        self._arg = arg

    def __call__(self, password1: str, password2: str):
        if password1 is not None and password2 is not None:

            if password1 == password2:
                
                return {"check": password1, "passwordIsValid": True, "passwordMustBeSent": True}

            else:
                
                return {"check": [password1, password2], "passwordIsValid": False}

        else:
            return {"check": "wait for password", "passwordMustBeSent": False}
