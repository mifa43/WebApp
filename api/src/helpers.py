import re

from decoraters import (CreateUserName, InputEmailIsEmail, InputMustBeLower,
                        PasswordIsEqualToPassword)


@InputMustBeLower
def checkNameAndEmail(name, email):
    """### Pomocna funkcija

       #### Pre izvrsavanja funkcije dekorater uzima argumente \
       i pretvara ih u mala slova i vraca u funkciju
    
        - :`name`
        - :`email`
    """
    return {"name": name, "email": email}

@InputEmailIsEmail
def emailValidation(email):
    """### Pomocna funkcija

       #### Pre izvrsavanja funkcije dekorater uzima argumente, \
        proverava da li je email validan i vraca u funkciju
    
        - :`email`
    """
    return email

@PasswordIsEqualToPassword
def checkPassword(password1, password2):
    """### Pomocna funkcija

       #### Pre izvrsavanja funkcije dekorater uzima argumente, \
        proverava da li su pass1 i pass2 isti i vraca u funkciju
    
        - :`password1`
        - :`password2`
    """
    return password1

@CreateUserName
def createUserName(firstName, lastName):
    """### Pomocna funkcija

       #### Pre izvrsavanja funkcije dekorater uzima argumente, \
        generise i vraca u funkciju spojene firstName i lastName
    
        - :`firstName`
        - :`lastName`
    """
    return (firstName, lastName)

