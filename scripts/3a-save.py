#!/bin/python36
#
# Nom : 3a-save.py
# Description : Script qui permet d’effectuer une sauvegarde
# Date : 06/11/2018
# Auteur : Jonathan DINH

##### IMPORTS #####

import sys
import signal
import shutil
import gzip
import os

##### VARIABLES #####

path_my_directory = os.path.expanduser('~/B2-Python')
path_data = os.path.expanduser('~/data')
path_my_backup = os.path.expanduser('~/backup_B2-Python')

##### FUNCTIONS #####

def youcant(sig, frame):
	goodbye()
	sys.exit(0)

def makeArchive(src_dir, archive_dir):
	shutil.make_archive(archive_dir, 'gztar', src_dir)

##### SCRIPT #####

signal.signal(signal.SIGINT, youcant)

if not os.path.exists(path_data):
	os.mkdir(path_data)

makeArchive(path_my_directory, path_my_backup)
path_my_backup += '.tar.gz'
#path_my_backup = os.path.expanduser('~/data/backup_B2-Python'+'.tar.gz')
if os.path.isfile(path_data + '/backup_B2-Python.tar.gz'):
	new_file = gzip.open(path_my_backup)
	old_file = gzip.open(path_data+'/backup_B2-Python.tar.gz')
	if new_file.read() == old_file.read():
		sys.stdout.write('Existe deja !\n')
		os.remove(path_my_backup)
	else:
		sys.stdout.write('Sauvegarder \n')
		os.remove(path_data+'/backup_B2-Python.tar.gz')
		shutil.move(path_my_backup, path_data)
else:
	shutil.move(path_my_backup, path_data)
