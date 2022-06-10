import re

class InputMustBeLower(object):
    # kreiranje dekoratera koji ce vratiti input malim slovima
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, name: str, email: str):
		lower = self._arg(name.lower(), email.lower())
		return lower

class InputEmailIsEmail(object):
	# kreiranje dekoratera sa re lib koji proverava da li je input email validan 
	def __init__(self, regex):
		"""
		### - regex lista simbola
		"""
		self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

	def __call__(self, email: str):
		"""na poziv dekoratera __call__ se izvrsava"""

		if (re.fullmatch(self.regex, email)):
			return {"EmailIsValid": True, "Email": email}

		else: 
			return {"EmailIsValid": False, "Email": None}

class PasswordIsEqualToPassword(object):
	def __init__(self, arg):
		"""### dekorater za proveru passworda
		
			- : `password1`
			- : `password2`

			#### ako je pass1 jedank pass2 vracamo `passwordIsValid`: `True`

		"""
		self._arg = arg

	def __call__(self, password1: str, password2: str):
		
		if password1 == password2:
			
			return {"check": password1, "passwordIsValid": True}

		else:
			
			return {"check": [password1, password2], "passwordIsValid": False}

class CreateUserName(object):
	def	__init__(self, arg):
			"""### dekorater za proveru passworda
		
			- : `userFirestName`
			- : `userLastName`

			#### username je kombinacija first i last name-a

		"""
			self._arg = arg

	def __call__(self, firstName: str, lastName: str):
		
		self._arg  = (firstName[0].upper() + firstName[1::] + "." + lastName[0].upper() + lastName[1::])
		return self._arg
		
		