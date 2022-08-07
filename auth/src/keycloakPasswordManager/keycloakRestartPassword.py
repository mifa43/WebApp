from keycloakPasswordManager.keycloakConnection import Connection
import json
class RestartPasswordKeycloak(Connection):

    def __init__(self, userID: str):

        self.userID = userID

        super().__init__()

    def user(self):

        # self.admin.realm_name = "demo" # vazno je da se prebacimo na realm demo
        
        response = self.admin.send_update_account(user_id=self.userID, payload=json.dumps(['UPDATE_PASSWORD'])) #{"user_id": userID, "payload": 'UPDATE_PASSWORD'}
        # restart = self.admin.set_user_password(user_id=userID, password=userNewPassword, temporary=True)
        return response