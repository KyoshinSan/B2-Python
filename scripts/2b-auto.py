#!/bin/python36
#
# Nom : 2b-auto.py
# Description : Résout 2a-mol
# Date : 06/11/2018
# Auteur : Jonathan DINH

##### IMPORTS #####

import random
import sys
import signal
import re
import time

##### VARIABLES #####

borneMin = 0
borneMax = 100
saisieBot = 50
welcomeMsg = "Bienvenue au jeu du plus ou moins ! Trouvez un nombre compris entre 0 et 100. Vous devez ecrire dans fichier un nombre !"
victoryMsg = 'Bravo, tu as gagne. La solution etait '
lessMsg = "C'est plus petit !"
moreMsg = "C'est plus grand !"

##### FUNCTIONS #####

def youcant(sig, frame):
	goodbye()
	sys.exit(0)

def lireFichier():
	fichier = open("./nombre.txt", "r")
	return fichier.read()
	fichier.close()

def ecrireFichier(text):
	text = str(text)
	fichier = open("./nombre.txt", "w")
	fichier.write(text)
	fichier.close()

def goodbye():
	print('\nLa solution était ' + str(saisieBot))
	print('***Goodbye !***')

##### SCRIPT #####

signal.signal(signal.SIGINT, youcant)
ecrireFichier(saisieBot)
time.sleep(1)
while True:
	if lireFichier() == victoryMsg + str(saisieBot):
		goodbye()
		break
	elif lireFichier() == lessMsg:
		borneMax = saisieBot
		saisieBot = borneMin + int((borneMax - borneMin)/2)
		ecrireFichier(saisieBot)
		time.sleep(1)
	elif lireFichier() == moreMsg:
		borneMin = saisieBot
		saisieBot = borneMin + int((borneMax - borneMin)/2)
		ecrireFichier(saisieBot)
		time.sleep(1)
	else:
		time.sleep(1)
