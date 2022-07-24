import random
import string

def recoveryCodeGenerator():
    # With combination of lower and upper case
    characters = string.ascii_letters + string.digits 
    code = ''.join(random.choice(characters) for i in range(8))

    # print random string
    return code
