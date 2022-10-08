import jwt


class TokenData():
    """### Klasa za dekodovanje tokena
       #### Kako bi se vratile informacije o korisniku \
       potrebno je dekodovati token koji dolazi sa FE-a
    
        - :`token` -> `keycloakUserID`
    """
    def __init__(self, token: str) -> None:
        self.token = token


    def decode(self):

        decoded = jwt.decode(self.token, options={"verify_signature": False})        

        print(decoded["sub"])

        return decoded["sub"]