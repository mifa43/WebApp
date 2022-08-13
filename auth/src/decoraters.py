import re, random
import asyncio

class PasswordIsEqualToPassword(object):
    """### dekorater za proveru passworda
        
            - : `password1`
            - : `password2`

            #### ako je pass1 jedank pass2 vracamo `passwordIsValid`: `True`

        """
    def __init__(self, arg):
        
        self._arg = arg

    def __call__(self, password1: str, password2: str):

        if password1 is not None and password2 is not None: # ako je pass1 i pass2 None nije dosao password
            # note: za restartovanje lozinke email je obavezan ali ako se korisnik seti lozinke ili iz nekog razloga odluci da ne iskoristi randomGenCode \
            # nema potrebe da se proverava i menja lozinka prsto se proces obustavlja

            if password1 == password2:  # pass1 i pass2 se podudaraju !
                
                return {"check": password1, "passwordIsValid": True, "passwordMustBeSent": True}

            else:   # lozinke nisu iste
                
                return {"check": [password1, password2], "passwordIsValid": False}

        else:   # cekaj password

            return {"check": "wait for password","passwordIsValid": False, "passwordMustBeSent": False}
