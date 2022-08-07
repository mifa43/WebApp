from keycloakPasswordManager.keycloakConnection import Connection

class GetKeycloakID(Connection):

    def __init__(self, userEmail: str):

        self.userEmail = userEmail

        super().__init__()

    def user(self):
        
        user_id_keycloak = self.admin.get_users({"email":f"{self.userEmail}"})
    
        if user_id_keycloak[0]["id"] == None:
    
            return {"exist" : False, "user_id_keycloak" : user_id_keycloak}

        else:

            return {"exist" : True, "user_id_keycloak" : user_id_keycloak}