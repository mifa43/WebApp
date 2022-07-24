import random
import string

def recoveryCodeGenerator() -> str:
    """ ### Kreiranje generatora kodova za restartovanje passworda
        __________________
        - return `code`
    
    """
    # kombinacija asci brojeva i slova, velikih i malih

    characters = string.ascii_letters + string.digits 

    #kod je duzine 8 karaktera i nasumicno generisan
    code = ''.join(random.choice(characters) for i in range(8))

    return code
