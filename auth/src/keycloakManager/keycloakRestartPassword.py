import asyncio
import json

from keycloakManager.keycloakConnection import Connection


class RestartPasswordKeycloak(Connection):
    """### Ova klasa je child i nasledjuje objekte za konekciju od parnet klase i salje email restart password 
    ______________________________________________
        - `userID`: Salje zahtev za restart password
    """
    def __init__(self, userID: str):

        self.userID = userID

        super().__init__()

    async def user(self):
        """### Salje request za restartovanje passworda
        """
        # self.keycloak_admin.realm_name = "demo"
        # self.admin.realm_name = "demo" # vazno je da se prebacimo na realm demo
        await asyncio.sleep(0)
        response = self.keycloak_admin.send_update_account(user_id=self.userID, payload=['UPDATE_PASSWORD']) #{"user_id": userID, "payload": 'UPDATE_PASSWORD'}

        # restart = self.admin.set_user_password(user_id=userID, password=userNewPassword, temporary=True)
        return response