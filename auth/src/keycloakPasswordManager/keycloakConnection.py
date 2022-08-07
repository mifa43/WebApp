from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os

class Connection:
    def __init__(self) -> None:
        
        self.admin = KeycloakAdmin(
            server_url="http://keycloak_keycloak_1:8080/auth/",
            username = "admin",
            password = "Pa55w0rd",
            realm_name = "master",
            verify = True)

        # Konektovanje na realm kao klijent

        self.openID = KeycloakOpenID(
            server_url = "http://keycloak_keycloak_1:8080/auth/",
            client_id = "appuser",
            realm_name = "demo",
            client_secret_key = "f550d47f-a4cd-41f3-ab0d-d72936b634af"
            )

        self.admin.realm_name = "demo"