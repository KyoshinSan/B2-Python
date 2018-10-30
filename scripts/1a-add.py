#!/bin/python36
#
# Nom : 1a-add.py
# Decription : Additionne 2 chiffre
# Date : 15/10/2018
# Auteur : Jonathan DINH et Theo HERNANDEZ

def addition(): #fonction addition
	while 0 < 1: #on boucle 
		try: #on test si input et un nombre si c'est vrai on casse la boucle
			int1 = int(input('Nombre 1 ? : '))
			break
		except ValueError: #sinon on affiche une erreur
			print("Erreur")
	
	while 0 < 1: #la même chose pour le 2eme nombre
		try:
			int2 = int(input('Nombre 2 ? : '))
			break
		except ValueError:
			print("Erreur")
	
	return int1 + int2 #on addition les 2 nombres

print('Le résultat est : ' + str(addition())) #affiche le résultat
