from decoraters import InputMustBeLower, InputEmailIsEmail, PasswordIsEqualToPassword

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
    return email

@PasswordIsEqualToPassword
def checkPassword(password1, password2):
    return password1
