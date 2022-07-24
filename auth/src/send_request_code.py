import requests
import os

class CreateCodeUserService():

    def __init__(self, email, code):

        self.email = email
        self.code = code

    def sendCode(self):
        url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/password-restart'

        data = {
            "UserEmail" : self.email,
            "code" : self.code
            }

        r = requests.post(url, json = data)

        return {"PostRequestSendOn": url, "code": self.code, "response": r.json()}