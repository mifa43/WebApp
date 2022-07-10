import asyncio
from requester import SendRequest
from crud import CreateKeycloakUser
async def foo(name: str, firstName: str, lastName: str, mail: str, phoneNumber: str, password: str):

    task = asyncio.create_task(SendRequest.userService(name, firstName, lastName, mail, phoneNumber, password))
    
    # await task
    w8 = await task
    
    yield w8

async def bzz(email: str, username: str, firstName: str, lastName: str, secret: str):

    task2 =await asyncio.create_task(CreateKeycloakUser().newUser(email, username, firstName, lastName, secret))
    
    # await task
    # w = await task2
    # return w
    # return {"clientID": "None", "userName": "None", "kcError":  "True"}

# async def grr(keycloak_id: str):

#     task3 = asyncio.create_task(CreateKeycloakUser().sendVerifyEmail(keycloak_id))
    
#     # await task
#     w3 = await task3
    
#     return w3