import asyncio

from keycloakManager.keycloakConnection import Connection


class UpdateUser(Connection):

    def __init__(self, keycloak_id: str) -> None:

        self.keycloak_id = keycloak_id

        super().__init__()

    async def send(self, payload: dict):
        """### Slanje email verifikacije nakon registracije
            - `keycloak_id`
        """
        self.admin.realm_name = "demo"
        
        # self.admin.realm_name = "demo"
        
        response = self.admin.update_user(
                user_id=self.keycloak_id,
                payload=payload)

        await asyncio.sleep(0)
        
        return {"update": True, "ID": self.keycloak_id}
            