"""
Does the following:
1. Inits git if used
2. Deletes dockerfiles if not going to be used
3. Deletes config utils if not needed
"""
from __future__ import print_function
import os
import shutil
from subprocess import Popen
from distutils.dir_util import copy_tree

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def copy_pkg(base_dir):
    copy_tree(base_dir, os.path.join(PROJECT_DIRECTORY))

if '{{ cookiecutter.base_pkg }}' != '':
    copy_pkg('{{ cookiecutter.base_pkg }}')
