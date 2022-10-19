import asyncio

from keycloakManager.keycloakConnection import Connection


class CreateUser(Connection):

    def __init__(self, email: str, username: str, firstName: str, lastName: str, secret: str) -> None:
        
        self.email = email
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.secret = secret

        super().__init__()

    async def new(self):
        """### Kreiranje korisnika na Keycloak
            - `email`
            - `username`
            - `firstName`
            - `lastName` 
            - `secret`
        """
              
        # Ulazimo u realm demo kao admin
 
        try:

            data = self.admin.create_user({
                "email": self.email,
                "username": self.username,
                "enabled": "True",
                "firstName": self.firstName,
                "lastName": self.lastName,
                "credentials": [
                    {
                        "value": self.secret,
                        "type": "password"
                    }
                ]
                })

            await asyncio.sleep(0)

            # sendEmail = await self.admin.send_verify_email(user_id=data)
           
            return {"clientID": data, "userName": self.username, "kcError":  False,"emailStatus": True, "ID": data}

        except:

            return {"clientID": None, "userName": None, "kcError":  True, "ID": False}