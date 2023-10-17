import os

from keycloak import KeycloakAdmin, KeycloakOpenID, KeycloakOpenIDConnection


class Connection:
    """### Keycloak klasa za konekciju
    ####  Ova klasa se ukljucuje u druge kao parent klasa child nasledjuje connection object
    ____________________________________________________________________________________
        - `admin`: konekcija za menadzovanje korisnika unutar realm-a
            - `self.admin.realm_name`: Za automatsko prebacivanje na realm za admin-a
        - `openID`: Konekcija za medadzovanje izvan realm-a npr(kreiranje novog realma)
        
    
    """
    def __init__(self) -> None:
        
        # Konektovanje kao admin na realm demo
        # U dokumentaciji za KeycloakOpenID kazu da treba /auth/ ali izgleda da to nije slucaj
        # Ovde se pise ime realma na kome je korisnik a ne admin samim tim koristi i demo:appuser i njegov secret -
        #  Ovo pravi veliku razliku od onog pre gde smo mogli sami da promenimo demo kao admin koristeci samo self.keycloak_admin.realm_name

        self.keycloak_openid = KeycloakOpenID(server_url=f"http://{os.getenv('KEYCLOAK_HOST')}:{os.getenv('KEYCLOAK_PORT')}",
                                 client_id=f"{os.getenv('KEYCLOAK_CLIENT_ID')}",
                                 realm_name="demo",
                                 client_secret_key=f"iuoMkXB95w4GSuNgIkFGswvpMaxRvkV7")

        # Konektovanje na realm kao klijent
        # U verziji keycloak 21+ se koristi KeycloakOpenIDConnection sa podatcima za autentifikaciju
        # Takoje u url path nema vise /auth/
        # KeycloakAdmin zahteva pristupni kljuc/toekn iz KeycloakOpenIDConnection
        # NAPOMENA: Keycloak zahteva autentifikaciju za realm master iz kog ulzi u self.keycloak_admin.realm_name = "demo" -
        #   potrebno je da je admin autorizovan - treba da udjes u realm setings i dodas roole, permisije za admina, user-a realm i client-a.
        self.keycloak_connection = KeycloakOpenIDConnection(
                                server_url=f"http://{os.getenv('KEYCLOAK_HOST')}:{os.getenv('KEYCLOAK_PORT')}/",
                                realm_name="master",
                                client_id=f"{os.getenv('KEYCLOAK_CLIENT_ID')}",
                                client_secret_key=f"{os.getenv('KEYCLOAK_CLIENT_SECRET_KEY')}")

        self.keycloak_admin = KeycloakAdmin(connection=self.keycloak_connection)

        # Budi siguran da si uvek na istom realm-u prilikom konektovanja
        self.keycloak_admin.realm_name = "demo"