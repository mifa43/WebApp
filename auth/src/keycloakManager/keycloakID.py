import asyncio

from keycloakManager.keycloakConnection import Connection


class GetKeycloakID(Connection):
    """### Ova klasa je child i nasledjuje objekte za konekciju od parnet klase i vraca keycloak userID 
    ______________________________________________
        - `userEmail`: Vraca userID ako postoji
    """
    def __init__(self, userEmail: str):

        self.userEmail = userEmail

        super().__init__()  # nasledjivanje parent klase

    async def user(self):
        """### Uzmi keycloak userID 
        """
        
        user_id_keycloak = self.admin.get_users({"email":f"{self.userEmail}"})

        await asyncio.sleep(0)

        if user_id_keycloak[0]["id"] == None:
    
            return {"exist" : False, "user_id_keycloak" : user_id_keycloak}

        else:

            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}