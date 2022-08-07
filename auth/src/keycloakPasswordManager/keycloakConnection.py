from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import os

class Connection:
    """### Keycloak klasa za konekciju
    ####  Ova kloasa se ukljucuje u druge kao parent klasa child nasledjuje connection object
    ____________________________________________________________________________________
        - `admin`: konekcija za menadzovanje korisnika unutar realm-a
            - `self.admin.realm_name`: Za automatsko prebacivanje na realm za admin-a
        - `openID`: Konekcija za medadzovanje izvan realm-a npr(kreiranje novog realma)
        
    
    """
    def __init__(self) -> None:
        
        # Konektovanje kao admin 

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

        # Budi siguran da si uvek na istom realm-u prilikom konektovanja

        self.admin.realm_name = "demo"