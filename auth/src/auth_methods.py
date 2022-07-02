from lib2to3.pgen2 import token
from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os

class KeycloakAuth():
    def __init__(self):

        # Kreiranje konekcije ka keycloak servisu

        self.admin = keycloak_admin = KeycloakAdmin(
                server_url="http://keycloak_keycloak_1:8080/auth/",
                username = "admin",
                password = "Pa55w0rd",
                realm_name = "master",
                verify = True)

        # Konektovanje na realm kao klijent

        self.openID = openID = KeycloakOpenID(
                server_url = "http://keycloak_keycloak_1:8080/auth/",
                client_id = "appuser",
                realm_name = "demo",
                client_secret_key = "f550d47f-a4cd-41f3-ab0d-d72936b634af"
                )

    def login(self, email: str, secret: str):

        """### Prijavljivanje (saljemo user creaditionale i dobijamo token)
            - `email`
            - `secret`
        """
        # Ulazimo u realm demo kao admin
        token = self.openID.token(email, secret)

        return token
    def logout(self, token: str):
    
        """### Prijavljivanje (saljemo user creaditionale i dobijamo token)
            - `token`
        """
        # Ulazimo u realm demo kao admin
        refToken = self.openID.logout(token)

        return refToken
    

    