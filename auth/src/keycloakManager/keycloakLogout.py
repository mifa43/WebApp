import asyncio

from keycloakManager.keycloakConnection import Connection


class Logout(Connection):
    """### Logout (`refresh_token` zatvaramo session ka keycloak-u token vise nije validan )
            - `token` == `refresh_token`
         ##### Ova klasa je child i nasledjuje objekte za konekciju od parnet klase i zatvara session
    """
    def __init__(self, token: str):

        self.token = token

        super().__init__()  # nasledjivanje parent klase

    async def refToken(self):
        
            """### Logout (`refresh_token` zatvaramo session ka keycloak-u token vise nije validan )
                - `token` == `refresh_token`
            """
            # Ulazimo u realm demo kao admin
            await asyncio.sleep(0)
            self.openID.logout(self.token)

            # return {"KeycloakAuthLogout": "The token was successfully submitted and the session was terminated"}