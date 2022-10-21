import asyncio
import os

import requests
import requests_async as requests


class SendRequest():
    """ ### Klasa koja sadrzi `POST` `PUT` `GET` METODE
        -`url`: prihvata svaki url
        -`session`: objekat koji je obotan async funkcijom

    """

    def __init__(self, url, session) -> None:
          
          self.url = url

          self.session = session

    def get(self, payload: str):
        """ ### Slanje GET Requesta na userservice
        
            ##### Ovo je malo dinamicnije jer kao parametar uzima
            -`payload`: u payload moze staviti razliciti formati json body-a
        """

        tasks = [] # lista

        tasks.append(asyncio.create_task(self.session.get(self.url, params = payload)))   # kreiramo corutine i dodajemo u listu

        return {"PostRequestSendOn": self.url, "Response": tasks}

    def post(self, payload: str):
            """ ### Slanje POST Requesta na userservice
        
            ##### Ovo je malo dinamicnije jer kao parametar uzima
            -`payload`: u payload moze staviti razliciti formati json body-a
            """


            tasks = [] # lista

            tasks.append(asyncio.create_task(self.session.post(self.url, json = payload)))   # kreiramo corutine i dodajemo u listu

            return {"PostRequestSendOn": self.url, "Response": tasks}

    def put(self, payload: str):
            """ ### Slanje PUT Requesta na userservice
        
            ##### Ovo je malo dinamicnije jer kao parametar uzima
            -`payload`: u payload moze staviti razliciti formati json body-a
            """

            tasks = [] # lista

            tasks.append(asyncio.create_task(self.session.put(self.url, json = payload)))   # kreiramo corutine i dodajemo u listu

            return {"PostRequestSendOn": self.url, "Response": tasks}
 