import asyncio

from keycloakManager.keycloakConnection import Connection


class Login(Connection):
    """### Login (saljemo user creaditionale i dobijamo token)
            - `email`
            - `secret`
        ##### Ova klasa je child i nasledjuje objekte za konekciju od parnet klase i vraca keycloak token 
    """
    def __init__(self, email: str, secret: str):

        self.email = email
        
        self.secret = secret

        super().__init__()  # nasledjivanje parent klase

    async def getToken(self):
        
        """### Login (saljemo user creaditionale i dobijamo token)
            - `email`
            - `secret`
        """
        self.keycloak_admin.realm_name = "demo"
        # Ulazimo u realm demo kao admin
        await asyncio.sleep(0)
        token = self.keycloak_openid.token(self.email, self.secret)

        return token

# login 0.5 logout 0.2