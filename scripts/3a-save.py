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
path_my_archive = os.path.expanduser('~/B2-Python'+'.tar.gz')

##### FUNCTIONS #####

def youcant(sig, frame):
	goodbye()
	sys.exit(0)

def makeArchive():
	shutil.make_archive(path_my_directory, 'gztar', path_data)

##### SCRIPT #####

signal.signal(signal.SIGINT, youcant)
os.mkdir(path_data)
makeArchive()
shutil.move(path_my_archive, path_data)
