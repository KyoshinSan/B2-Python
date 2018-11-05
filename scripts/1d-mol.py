#!/bin/python36
#
# Nom : 1d-mol.py
# Description : Jeu du plus ou moins
# Date : 23/10/2018
# Auteur : Jonathan DINH

##### IMPORTS #####

from random import randint
import sys
import signal

##### VARIABLES #####

nombreAleatoire = randint(0,100)

##### FUNCTIONS #####

def youcant(sig, frame):
	goodbye()
	sys.exit(0)

def checkIsNumber():
	while True:
		try:
			saisie = input('Saisir un nombre, taper \'q\' pour quitter : ')
			if saisie == 'q':
				break
			saisie = int(saisie)
			if saisie > 100 or saisie < 0:
				print('Erreur ce nombre n\'est pas compris entre 0 et 100')
			else:
				break
		except ValueError:
			print('Erreur ce n\'est pas un nombre')
	return saisie

def goodbye():
	print('\nLa solution était ' + str(nombreAleatoire))
	print('***Goodbye !***')

##### SCRIPT #####

signal.signal(signal.SIGINT, youcant)

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
