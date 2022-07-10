import  requests,os, asyncio
import requests_async as requests
class SendRequest():

    async def userService(name: str, firstName: str, lastName: str, mail: str, phoneNumber: str, password: str):
        """Slanje Requesta na userservice"""
      

        #docker container ce biti u env variabli
        # await asyncio.sleep(0)
        url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/insert-user'

        # request body

        data = {
            "UserName" : name,
            "UserFirstName" : firstName,
            "UserLastName" : lastName,
            "UserEmail" : mail,
            "UserNumber" : phoneNumber,
            "UserPassword" : password
            }
        async with requests.Session() as session:
            response = await session.post(url, json = data)
            
            
        # response = requests.post(url, json = data)
        
            # await asyncio.sleep(2)
        return {"PostRequestSendOn": url, "Response": response.json()}    # url se brise ovo je za test fazu, lakse dizanje excep-a, debug i loggove

    
