import asyncio

from keycloakManager.keycloakConnection import Connection


class CreateUser(Connection):

    def __init__(self, email: str, secret: str) -> None:
        
        self.email = email
        self.secret = secret

        super().__init__()

    async def new(self):
        """### Kreiranje korisnika na Keycloak
            - `email`
            - `username`
            - `secret`
        """
              
        # Ulazimo u realm demo kao admin
        print(self.email, self.secret)
        try:
            self.keycloak_admin.realm_name = "demo"
            data = self.keycloak_admin.create_user({
                "email": self.email,
                "username": self.email,
                "enabled": "True",
                "firstName": None,
                "lastName": None,
                "credentials": [
                    {
                        "value": self.secret,
                        "type": "password"
                    }
                ]
                })

            await asyncio.sleep(0)

            # sendEmail = await self.admin.send_verify_email(user_id=data)
            print(data)
            return {"clientID": data, "userName": self.email, "kcError":  False,"emailStatus": True, "ID": data}

        except:

            return {"clientID": None, "userName": None, "kcError":  True, "ID": False}