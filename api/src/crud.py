from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os

class CreateKeycloakUser():
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

    def newUser(self, email: str, username: str, firstName: str, lastName: str, secret: str):
        """### Kreiranje korisnika na Keycloak
            - `email`
            - `username`
            - `firstName`
            - `lastName` 
            - `secret`
        """
        
        
        # Ulazimo u realm demo kao admin

        self.admin.realm_name = "demo"
        
        try:
            data = self.admin.create_user({
                "email": email,
                "username": username,
                "enabled": "True",
                "firstName": firstName,
                "lastName": lastName,
                "credentials": [
                    {
                        "value": secret,
                        "type": "password"
                    }
                ]
                })
        
            return {"clientID": data, "userName": username, "kcError":  False}

        except:

            return {"clientID": None, "userName": None, "kcError":  True}

    def getKeycloakUserID(self, username: str):
        """### Uzmi keycloak user id 
            - `username`
        """
        self.admin.realm_name = "demo"

        keycloakUserID = self.admin.get_user_id(username)
     
        return {"ID": keycloakUserID, "keycloakUser": username}
        

    def sendVerifyEmail(self, keycloak_id: str):
        """### Slanje email verifikacije nakon registracije
            - `keycloak_id`
        """
        
        self.admin.realm_name = "demo"

        sendEmail = self.admin.send_verify_email(user_id=keycloak_id)

        if keycloak_id == None:

            return {"ID": False}

        else: 

            return {"emailStatus": True, "ID": keycloak_id}
