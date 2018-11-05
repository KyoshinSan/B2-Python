#!/bin/python36

# Nom : 1c-moy.py
# Description : Saisie de pusieur note et prenom, Affichage moyenne et top 5 note
# Date : 15/10/2018
# Auteur : Jonathan DINH

##### VARIABLES #####

my_dict = {}
listeNote = []

def checkIsNumber():
	while True:
		try:
			note = int(input('Saisir la note de l\'élève : '))
			if note > 20 or note < 0:
				print('Erreur ce nombre n\'est pas compris entre 0 et 20')
			else:
				break
		except ValueError:
			print('Erreur ce n\'est pas un nombre')
	return note

def afficherMoyenne():
	moyenne = 0
	nbrNote = 0
	for val in my_dict.values():	#on prend la note dans le dictionnaire que l'on ajoute a la variable moyenne
		moyenne += val
		nbrNote += 1
	return(moyenne/nbrNote)		#on return la moyenne

def triTop5Note():
	x = 0
	print('Le top 5 des meilleurs note : ')
	for k, v in listeNote:	#pour chaque note dans notre liste on va afficher le prénom et la note
		print('Prenom: ' + k + ', Note: ' + str(v))
		x +=1
		if x == 5:	#dès qu'on est a 5 on casse la boucle pour avoir que les 5 premières notes
			break

##### SCRIPT #####

while True:
	prenom = input('Saisir un prenom, taper \'q\' pour quitter : ')
	if prenom == 'q':
		break
	my_dict[prenom] = checkIsNumber()

listeNote = [(k, my_dict[k]) for k in sorted(my_dict, key=my_dict.get, reverse=True)] 	#cette liste permet de trier et convertir le dictionnaire en liste
print('La moyenne de classe est de : ' + str(afficherMoyenne())) #on affiche la moyenne
triTop5Note() #on affiche le top 5 des notes
