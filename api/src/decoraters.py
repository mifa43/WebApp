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

		

