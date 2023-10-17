import os

from keycloak import KeycloakAdmin, KeycloakOpenID, KeycloakOpenIDConnection


class ResendVerifyEmail():
    
    def __init__(self):
        # Konektovanje kao admin 

        self.keycloak_openid = KeycloakOpenID(server_url=f"http://{os.getenv('KEYCLOAK_HOST')}:{os.getenv('KEYCLOAK_PORT')}/",
                                 client_id=f"{os.getenv('KEYCLOAK_CLIENT_ID')}",
                                 realm_name="master",
                                 client_secret_key=f"{os.getenv('KEYCLOAK_CLIENT_SECRET_KEY')}")

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

    def getKeycloakUserID(self, username):
        """
        ### Uzmi Keycloak user id.
        
        ---------------
            - `user_id_keycloak` -> `username` : None -> bool(False) - ako nema username
            - `user_id_keycloak` -> `username` : bool(True), user_id - ima username
        """

        self.keycloak_admin.realm_name = "demo"

        user_id_keycloak = self.keycloak_admin.get_user_id(username)

        if user_id_keycloak == None:

            return {"exist" : False}

        else:

            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}

    def sendVerification(self, user_id_keycloak):
        """ ### Ponovo posalji email verifikaciju.
            - `user_id_keycloak` -> param
            - `send_verify_email` -> slanje verifikacije
        """

        self.keycloak_admin.realm_name = "demo"
        # user_id_keycloak dobijamo iz prethodne funkcije koju saljemo iz main fajla
        self.keycloak_admin.send_verify_email(user_id=user_id_keycloak)
