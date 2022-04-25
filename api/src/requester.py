from urllib import response
import requests

class SendRequest():
    """Slanje Requesta na userservice"""
    def userService(name: str, lastName: str, mail: str, phoneNumber: int, password: str):
        
        url = 'http://fastapi_userservice:8080/insert-user'
        data = {
            "UserName" : name,
            "UserLastName" : lastName,
            "UserEmail" : mail,
            "UserNumber" : phoneNumber,
            "UserPassword" : password
            }
        response = requests.post(url, json = data)

        return {"PostRequestSendOn": url, "Response": response.json()}    # url se brise ovo je za test fazu, lakse dizanje excep-a, debug i loggove