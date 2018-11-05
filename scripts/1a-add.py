#!/bin/python36
#
# Nom : 1a-add.py
# Decription : Additionne 2 chiffre
# Date : 15/10/2018
# Auteur : Jonathan DINH

##### FONCTION #####

def addition():
	while True:
		try:
			int1 = int(input('Nombre 1 ? : '))
			break
		except ValueError:
			print("Erreur")
		""" On test notre input avec un try,
		si le nombre est entier on casse la boucle,
		sinon cela affiche erreur et on doit retaper un nombre.
		"""
	
#la même chose pour le 2eme nombre

	while True:
		try:
			int2 = int(input('Nombre 2 ? : '))
			break
		except ValueError:
			print("Erreur")
	
	return int1 + int2

##### SCRIPT #####

print('Le résultat est : ' + str(addition()))
