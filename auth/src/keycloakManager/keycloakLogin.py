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

    def getToken(self):
        
        """### Login (saljemo user creaditionale i dobijamo token)
            - `email`
            - `secret`
        """
        # Ulazimo u realm demo kao admin
        token = self.openID.token(self.email, self.secret)

        return token