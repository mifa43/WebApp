import re

class ModelToDict(object):
	"""Konvertovanjer tuple-a u dict"""
    # kreiranje dekoratera koji ce vratiti fastapi model kao dict
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, tup: tuple):
		# lista kako bi smo dobili metodu append
		lis = []
		
		for i in tup:
			
			lis.append(i)   # dodajemo svaki par tuple-a, 1 par = [('name', 'Joe'), ('lastname', 'Doe')]

			x = tuple(lis)  #elemente liste konvertujemo u tuple
			
			dic = self._arg(dict((key, value) for key, value in x)) #for rastavlja iz tuple-a key, vale i vraca kao dict
			
		return dic
