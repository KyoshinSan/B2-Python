#!/usr/bin/python36
# -*- coding: utf-8 -*-

# Nom : 1c-moy.py
# Description : Saisie de pusieur note et prenom, Affichage moyenne et top 5 note
# Date : 15/10/2018
# Auteur : Jonathan DINH

##### VARIABLES #####

my_dict = {}
listeNote = []

##### FONCTIONS #####

def checkIsNumber():
    while True:
        try:
            note = int(input('Saisir la note de l\'eleve : '))
            if note > 20 or note < 0:
                print('Erreur ce nombre n\'est pas compris entre 0 et 20')
            else:
                break
        except ValueError:
            print('Erreur ce n\'est pas un nombre')
    return note


def afficherMoyenne():
    totalNote = 0
    nbrNote = 0
    for val in my_dict.values():
        totalNote += val
        nbrNote += 1
    return totalNote / nbrNote


def triTop5Note():
    x = 0
    print('Le top 5 des meilleurs note : ')
    for (k, v) in listeNote:
        print('Prenom: ' + k + ', Note: ' + str(v))
        x += 1
        if x == 5:
            break


##### SCRIPT #####

while True:
    prenom = input('Saisir un prenom, taper \'q\' pour quitter : ')
    if prenom == 'q':
        break
    my_dict[prenom] = checkIsNumber()

# cette liste permet de trier et convertir le dictionnaire en liste

listeNote = [(k, my_dict[k]) for k in sorted(my_dict, key=my_dict.get, reverse=True)]

# on affiche la moyenne

print('La moyenne de classe est de : ' + str(afficherMoyenne()))

# on affiche le top 5 des notes

triTop5Note()
