#!/usr/bin/python36
# -*- coding: utf-8 -*-

# Nom : 1b-dic.py
# Description : liste de prenom trier par ordre alphabetique
# Date : 15/10/2018
# Auteur : Jonathan DINH

##### VARIABLES #####

liste = []

##### SCRIPT #####

while True:
    prenom = input('Saisir un prenom, taper \'q\' pour quitter : ')
    if prenom == 'q':
        break
    liste.append(prenom)

print(sorted(liste))
