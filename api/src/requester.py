import asyncio
import os

import requests
import requests_async as requests


class SendRequest():

    def userService(mail: str, keycloakUserID: str, session):
        """Slanje Requesta na userservice"""
      

        #docker container ce biti u env variabli
        # await asyncio.sleep(0)
        url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/insert-user'

        # request body

        data = {
            "UserEmail" : mail,
            "keycloakUserID" : keycloakUserID
            }

        tasks = [] # lista

        tasks.append(asyncio.create_task(session.post(url, json = data)))   # kreiramo corutine i dodajemo u listu

        return {"PostRequestSendOn": url, "Response": tasks}

        # # response = requests.post(url, json = data)
        
        #     # await asyncio.sleep(2)
        # return {"PostRequestSendOn": url, "Response": response.json()}    # url se brise ovo je za test fazu, lakse dizanje excep-a, debug i loggove

    
