#!/bin/python36
#
# Nom : 1d-mol.py
# Description : Jeu du plus ou moins
# Date : 23/10/2018
# Auteur : Jonathan DINH

from random import randint
import sys
import signal

def youcant(sig, frame):
	goodbye()
	sys.exit(0)

signal.signal(signal.SIGINT, youcant)
signal.signal(signal.SIGTERM, youcant)

nombreAleatoire = randint(0,100)

def checkIsNumber():	#fonction qui test si l'input est une note
	while True:
		try:
			saisie = input('Saisir un nombre, taper \'q\' pour quitter : ')
			if saisie == 'q':
				break
			saisie = int(saisie)
			if saisie > 100 or saisie < 0:       #condition qui vérifie si la saisie est entre 0 et 100
				print('Erreur ce nombre n\'est pas compris entre 0 et 100')
			else:
				break
		except ValueError:
			print('Erreur ce n\'est pas un nombre')
	return saisie

def goodbye():
	print('\nLa solution était ' + str(nombreAleatoire))
	print('***Goodbye !***')

while True:
	nombreUser = checkIsNumber()
	
	if nombreUser == 'q':
		goodbye()
		break
	if nombreUser == nombreAleatoire:
		break
	elif nombreUser > nombreAleatoire:
		print('C\'est plus petit !')
	else:
		print('C\'est plus grand !')
