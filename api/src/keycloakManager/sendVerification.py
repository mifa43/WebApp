import asyncio

from keycloakManager.keycloakConnection import Connection


class SendVerification(Connection):

    def __init__(self, keycloak_id: str) -> None:

        self.keycloak_id = keycloak_id

        super().__init__()

    async def send(self):
        """### Slanje email verifikacije nakon registracije
            - `keycloak_id`
        """
        self.admin.realm_name = "demo"
        
        # self.admin.realm_name = "demo"
        
        sendEmail = self.admin.send_verify_email(user_id=self.keycloak_id)
        await asyncio.sleep(0)
        if self.keycloak_id == None:

            return {"ID": False}

        else: 
            
            return {"emailStatus": True, "ID": self.keycloak_id}
            