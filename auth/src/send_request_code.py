from http.client import responses
import requests
import os

class CreateCodeUserService():
    """ ### slanje requesta na userservice za restartovanje passworda
    __________________________________
    - `email` -> registrovani email *samo ako postoji
    - `code` -> randomCodeGen *upisuje se u db radi kasnije provere
    
    """
    def __init__(self, email, code):

        self.email = email
        self.code = code

    def sendCode(self) -> str:
        """ ### Posalji request 
        _________
        - `url` -> docker service url *HOST:PORT
        - `data` -> json body param *EMAIL:CODE
        """
        # docker url
        url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/password-restart'

        # data body
        data = {
            "UserEmail" : self.email,
            "code" : self.code
            }

        # r Response
        r = requests.post(url, json = data)

        return {"PostRequestSendOn": url, "code": self.code, "response": r.json()}