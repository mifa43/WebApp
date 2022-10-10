import  requests,os, asyncio
import requests_async as requests

class SendRequest():

    def userService(keycloakUserID: str, session):
        """Slanje Requesta na userservice"""
      

        #docker container ce biti u env variabli
        # await asyncio.sleep(0)
        url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/get-user'

        # request body

        data = {
            "keycloakUserID" : keycloakUserID
            }

        tasks = [] # lista

        tasks.append(asyncio.create_task(session.get(url, params= data)))   # kreiramo corutine i dodajemo u listu

        return {"PostRequestSendOn": url, "Response": tasks}

    def userServiceUpdate(imageUrl: str, keycloakUserID: str, session):
            """Slanje Requesta na userservice"""
        

            #docker container ce biti u env variabli
            # await asyncio.sleep(0)
            url = f'http://{os.getenv("USERSERVICE_HOST")}:{os.getenv("USERSERVICE_PORT")}/update-user-image'

            # request body

            data = {
                "imageUrl" : imageUrl,
                "keycloakUserID" : keycloakUserID
                }

            tasks = [] # lista

            tasks.append(asyncio.create_task(session.post(url, json = data)))   # kreiramo corutine i dodajemo u listu

            return {"PostRequestSendOn": url, "Response": tasks}
