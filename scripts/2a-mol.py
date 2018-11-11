#!/usr/bin/python36
# -*- coding: utf-8 -*-

# Nom : 2a-mol.py
# Description : Plus ou moins avec lecture dans un fichier
# Date : 23/10/2018
# Auteur : Jonathan DINH

##### IMPORTS #####

import random
import time
import sys
import signal

##### VARIABLES #####

nombreAleatoire = random.randint(0, 100)
welcomeMsg = 'Bienvenue au jeu du plus ou moins ! Trouvez un nombre compris entre 0 et 100. Vous devez ecrire dans fichier un nombre !'
moreMsg = "C'est plus grand !"
lessMsg = "C'est plus petit !"
victoryMsg = 'Bravo, tu as gagne. La solution etait ' + str(nombreAleatoire)


##### FONCTIONS #####

def youcant(sig, frame):
    goodbye()
    sys.exit(0)


def EcrireMsgBienvenue():
    fichier = open('./nombre.txt', 'w')
    fichier.write(welcomeMsg)
    fichier.close()


def lectureNombre():
    fichier = open('./nombre.txt', 'r')
    return fichier.read()
    fichier.close()


def EcrirePlusPetit():
    fichier = open('./nombre.txt', 'w')
    fichier.write(lessMsg)
    fichier.close()


def EcrirePlusGrand():
    fichier = open('./nombre.txt', 'w')
    fichier.write(moreMsg)
    fichier.close()


def EcrireVictoire():
    fichier = open('./nombre.txt', 'w')
    fichier.write(victoryMsg)
    fichier.close()


def goodbye():
    print('\nLa solution etait ' + str(nombreAleatoire))
    print('***Goodbye !***')


##### SCRIPT ######

signal.signal(signal.SIGINT, youcant)
signal.signal(signal.SIGTERM, youcant)

EcrireMsgBienvenue()

while True:
    saisie = lectureNombre()
    try:
        saisie = int(saisie)
        if saisie == nombreAleatoire:
            EcrireVictoire()
            break
        elif saisie > nombreAleatoire:
            EcrirePlusPetit()
            time.sleep(1)
        else:
            EcrirePlusGrand()
            time.sleep(1)
    except ValueError:
        time.sleep(1)
