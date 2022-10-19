import os

from keycloak import KeycloakAdmin, KeycloakOpenID


class Connection:
    """### Keycloak klasa za konekciju
    ####  Ova klasa se ukljucuje u druge kao parent klasa child nasledjuje connection object
    ____________________________________________________________________________________
        - `admin`: konekcija za menadzovanje korisnika unutar realm-a
            - `self.admin.realm_name`: Za automatsko prebacivanje na realm za admin-a
        - `openID`: Konekcija za medadzovanje izvan realm-a npr(kreiranje novog realma)
        
    
    """
    def __init__(self) -> None:
        
        # Konektovanje kao admin 

        self.admin = KeycloakAdmin(
            server_url= f"http://{os.getenv('KEYCLOAK_HOST')}:{os.getenv('KEYCLOAK_PORT')}/auth/",
            username = f"{os.getenv('KEYCLOAK_USER')}",
            password = f"{os.getenv('KEYCLOAK_PASSWORD')}",
            realm_name = "master",
            verify = True)

        # Konektovanje na realm kao klijent

        self.openID = KeycloakOpenID(
            server_url = f"http://{os.getenv('KEYCLOAK_HOST')}:{os.getenv('KEYCLOAK_PORT')}/auth/",
            client_id = f"{os.getenv('KEYCLOAK_CLIENT_ID')}",
            realm_name = "demo",
            client_secret_key = f"{os.getenv('KEYCLOAK_CLIENT_SECRET_KEY')}"
            )

        # Budi siguran da si uvek na istom realm-u prilikom konektovanja

        self.admin.realm_name = "demo"