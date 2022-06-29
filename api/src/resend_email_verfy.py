from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os

class ResendVerifyEmail():
    
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

    def getKeycloakUserID(self, username):
        """
        ### Uzmi Keycloak user id.
        
        ---------------
            - `user_id_keycloak` -> `username` : None -> bool(False) - ako nema username
            - `user_id_keycloak` -> `username` : bool(True), user_id - ima username
        """

        self.admin.realm_name = "demo"

        user_id_keycloak = self.admin.get_user_id(username)

        if user_id_keycloak == None:

            return {"exist" : False}

        else:

            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}

    def sendVerification(self, user_id_keycloak):
        """ ### Ponovo posalji email verifikaciju.
            - `user_id_keycloak` -> param
            - `send_verify_email` -> slanje verifikacije
        """

        self.admin.realm_name = "demo"
        # user_id_keycloak dobijamo iz prethodne funkcije koju saljemo iz main fajla
        self.admin.send_verify_email(user_id=user_id_keycloak)
