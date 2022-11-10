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

		l = {}	# prazan dict u koji se upisuju vrednosti koje su razlicite od None

		for key in list(dic.keys()):	# forujemo dict koji je force konvertovan u listu kako bi izbegli gresku: RuntimeError: dictionary changed size during iteration

			if dic[key] == None:	# ako je vrednost key-a jednaka None

				del dic[key]	# brisem key koji je None

			else:	# ako je bilo koja vrednost osim None, dodajemo je u novi dict kao kopiju i smatramo je validnom za update body
		
				l[key] = dic[key]	# kopiraj key i value u novi dict

		return l
