import re

from decoraters import (ModelToDict)


@ModelToDict
def modelToDict(body):
    """### Pomocna funkcija

       #### Pre izvrsavanja funkcije dekorater uzima argumente \
       i konvertuje model u dict
    
        - :`body`: fastapi model
        - :`retrn`: dict
    """
    return body

# model = (('UserFirstName', 'mifa43'),('UserLastName', 'kotez23'),('UserEmail', 'mifa43kotez@gmail.com'),('UserNumber', '131313131313'),('keycloakUserID', '4253c73b-0fab-48e3-91d7-d3a7540605ef'))

# d = modelToDict(model)

# print(d)