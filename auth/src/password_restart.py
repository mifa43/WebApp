from lib2to3.pgen2 import token
from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os

class KeycloakUserPasswordManage():
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

    def getKeycloakUserId(self, userEmail: str):
        
        self.admin.realm_name = "demo"

        user_id_keycloak = self.admin.get_user_id(userEmail)

        if user_id_keycloak == None:
    
            return {"exist" : False}

        else:

            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}

    def restartPassword(self, userID: str, userNewPassword: str):

        restart = self.admin.set_user_password(user_id=userID, password=userNewPassword, temporary=True)
