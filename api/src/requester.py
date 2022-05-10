from urllib import response
import requests, os

class SendRequest():

    def userService(name: str, lastName: str, mail: str, phoneNumber: str, password: str):
        """Slanje Requesta na userservice"""

        #docker container ce biti u env variabli

        url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/insert-user'

        # request body

        data = {
            "UserName" : name,
            "UserLastName" : lastName,
            "UserEmail" : mail,
            "UserNumber" : phoneNumber,
            "UserPassword" : password
            }
        response = requests.post(url, json = data)

        return {"PostRequestSendOn": url, "Response": response.json()}    # url se brise ovo je za test fazu, lakse dizanje excep-a, debug i loggove