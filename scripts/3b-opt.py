#!/usr/bin/python36
# -*- coding: utf-8 -*-

# Nom : 3b-opt.py
# Description : Script qui permet d effectuer une sauvegarde avec des option au lancement
# Date : 10/11/2018
# Auteur : Jonathan DINH

##### IMPORTS #####

import sys
import signal
import shutil
import gzip
import os
import argparse

##### VARIABLES #####

parser = argparse.ArgumentParser(description='creer une sauvegarde d un repertoire vers un autre')
parser.add_argument('path_my_directory', help='Indiquer le chemin du repertoire que vous voulez archiver')
parser.add_argument('path_data', help='Indiquer le chemin du repertoire de /data')
args = parser.parse_args()

path_my_directory = args.path_my_directory
path_data = args.path_data + '/data'
path_my_backup = '/tmp/backup'

msgErrorPerm = 'Vous n\'avez pas la permission !'
msgSaved = 'Sauvegarde effectuer !\n'
msgSavedExisting = 'Votre sauvegarde existe deja !\n'


##### FUNCTIONS #####

def youcant(sig, frame):
    if os.path.isfile(path_my_backup):
        os.remove(path_my_backup)
    sys.stdout('Sauvegarde annuler !\n')
    sys.exit(0)


def makeArchive(src_dir, archive_dir):
    if os.access(src_dir, os.R_OK):
        shutil.make_archive(archive_dir, 'gztar', src_dir)
    else:
        sys.stderr.write(msgErrorPerm + ' (repertoire source)\n')


##### SCRIPT #####

signal.signal(signal.SIGINT, youcant)

if os.access(args.path_data, os.R_OK and os.W_OK):

    if not os.path.isdir(path_data):
        os.mkdir(path_data)

    try:
        makeArchive(path_my_directory, path_my_backup)
        path_my_backup += '.tar.gz'

        if os.path.isfile(path_data + '/backup.tar.gz'):
            new_file = gzip.open(path_my_backup)
            old_file = gzip.open(path_data + '/backup.tar.gz')
            if new_file.read() == old_file.read():
                sys.stdout.write(msgSavedExisting)
                os.remove(path_my_backup)
            else:
                os.remove(path_data + '/backup.tar.gz')
                shutil.move(path_my_backup, path_data)
                sys.stdout.write(msgSaved)
        else:
            shutil.move(path_my_backup, path_data)
            sys.stdout.write(msgSaved)
    except:
        sys.stderr.write('L\'archive n\'a pu etre creer a cause d\'une erreur\n')
        sys.exit(0)
else:

    sys.stderr.write(msgErrorPerm + ' (repertoire de destination)\n')

