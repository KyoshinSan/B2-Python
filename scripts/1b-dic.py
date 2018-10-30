#!/bin/python36

# Nom : 1b-dic.py
# Description : liste de prenom trier par ordre alphabetique
# Date : 15/10/2018
# Auteur : Theo HERNANDEZ et Jonathan DINH

liste = [] 	#on déclare notre liste

while 0 < 1: 	#on boucle notre inpupt
	prenom = input('Saisir un prenom, taper \'q\' pour quitter : ')
	if prenom == 'q': 	#si l'input est q alors on quitte la boucle
		break
	liste.append(prenom) 	#sinon on ajoute à la liste

print(sorted(liste)) 	#on affiche la liste trier avec la fonction sorted
