from decoraters import InputMustBeLower

@InputMustBeLower
def checkNameAndEmail(name, email):
    """### Pomocna funkcija

       #### Pre izvrsavanja funkcije dekorater uzima argumente \
       i pretvara ih u mala slova i vraca u funkciju
    
        - :`name`
        - :`email`
    """
    return {"name": name, "email": email}
