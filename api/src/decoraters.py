
class InputMustBeLower(object):
    # kreiranje dekoratera koji ce vratiti input malim slovima
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, name: str, email: str):
		lower = self._arg(name.lower(), email.lower())
		return lower