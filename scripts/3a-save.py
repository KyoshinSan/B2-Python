#!/usr/bin/python36
# -*- coding: utf-8 -*-

# Nom : 3a-save.py
# Description : Script qui permet d effectuer une sauvegarde
# Date : 06/11/2018
# Auteur : Jonathan DINH

##### IMPORTS #####

import sys
import signal
import shutil
import gzip
import os

##### VARIABLES #####

path_my_directory = '/root/B2-Python'
path_data = '/root/data'
path_my_backup = '/tmp/backup_B2-Python'

msgErrorPerm = 'Vous n\'avez pas la permission !\n'
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
        sys.stderr.write(msgErrorPerm)


##### SCRIPT #####

signal.signal(signal.SIGINT, youcant)

if os.access('/root', os.R_OK and os.W_OK):

    if not os.path.isdir(path_data):
        os.mkdir(path_data)

    makeArchive(path_my_directory, path_my_backup)
    path_my_backup += '.tar.gz'

    if os.path.isfile(path_data + '/backup_B2-Python.tar.gz'):
        new_file = gzip.open(path_my_backup)
        old_file = gzip.open(path_data + '/backup_B2-Python.tar.gz')

        if new_file.read() == old_file.read():
            sys.stdout.write(msgSavedExisting)
            os.remove(path_my_backup)
        else:
            os.remove(path_data + '/backup_B2-Python.tar.gz')
            shutil.move(path_my_backup, path_data)
            sys.stdout.write(msgSaved)
    else:

        shutil.move(path_my_backup, path_data)
        sys.stdout.write(msgSaved)
else:

    sys.stderr.write(msgErrorPerm)
