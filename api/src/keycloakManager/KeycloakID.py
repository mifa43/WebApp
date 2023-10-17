import asyncio

from keycloakManager.keycloakConnection import Connection


class GetKeycloakID(Connection):

    def __init__(self, username) -> None:

        self.username = username

        super().__init__()

    async def userID(self):
        """
        ### Uzmi Keycloak user id.
        
        ---------------
            - `user_id_keycloak` -> `username` : None -> bool(False) - ako nema username
            - `user_id_keycloak` -> `username` : bool(True), user_id - ima username
        """

        self.keycloak_admin.realm_name = "demo"

        user_id_keycloak = self.keycloak_admin.get_user_id(self.username)

        await asyncio.sleep(0)
        
        if user_id_keycloak == None:

            return {"exist" : False}

        else:

            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}
