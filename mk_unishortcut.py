#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:24:02 2017
@author: cassani
"""

import sys
import os
import posix
import posixpath as path
import stat

# Usage text 
usage_text = 'Usage: mk_unishortcut.py <target>'
# Help text = ''

# Working directory
working_dir = os.getcwd()

# Number of arguments
n_argv = len(sys.argv) 

# Validate Inputs
if n_argv == 1:
    print(usage_text)
    # Return error
elif n_argv == 2:
    posix_arg = str(sys.argv[1]).replace("\\", "/")
    targetpath = path.abspath(posix_arg)
else:
    print(usage_text)
    # Return error

if not(path.exists(targetpath)):
    print("The target '" + targetpath + "' does not exist")
    # Return error

# Create path to shortcutfile
shortcutpath = path.join(working_dir, str(path.basename(targetpath)) + '.cmd')

if (path.exists(shortcutpath)):
    print("The shortcut file '" + shortcutpath + "' already exist")
    print("Do you want to replace it?")
#TODO give the option ot the user to decide

# Find the relation between targetpath and working directory
rel_targetpath = path.relpath(targetpath, start=working_dir)

# Split relative target path into directory and file
[rel_directory, rel_file] = os.path.split(rel_targetpath)
print(rel_directory + rel_file)

# Desktop Environment: [Extended Regular Expression , start-like command
environments_dict = {'Cinnamon': ["'^.* cinnamon$'     ", 'gvfs-open'], 
                     'KDE'     : ["'^.* kded4$'        ", ''], 
                     'UNITY'   : ["'unity-panel'       ", 'gvfs-open'], 
                     'XFCE'    : ["'^.* xfce4-session$'", ''], 
                     'MATE'    : ["'^.* mate-panel$'   ", ''], 
                     'LXDE'    : ["'^.* lxsession$'    ", ''], 
                     'MacOSX'  : ["'^.*Aqua[^\$]$'     ", 'open']
                     }
# Dictionary based on work from https://github.com/alexeevdv/dename/blob/master/dename.sh    

# Create shortcut file
shortcutfile = open(shortcutpath, 'w' , newline='\n')
# Linux part 
shortcutfile.write(':; # Linux part' + '\n')
for key, value in environments_dict.items():
    shortcutfile.write(':; ' + 'ps -e | grep -E ' + value[0] + ' > /dev/null ' 
                       + '&& ' + value[1] + ' ' + "'" + rel_targetpath + "'" + ' ' + 
                       + '&& ' + 'exit' + '\n')   

shortcutfile.write('\n')
# Windows part
shortcutfile.write(':: # Windows part\n')
shortcutfile.write('@ECHO OFF\n')
shortcutfile.write('cd "' + rel_directory + '"' + '\n')
shortcutfile.write('start ' +'""' + ' ' + '"' + rel_file + '"' + '\n') 
shortcutfile.write('EXIT\n') 
shortcutfile.close() 

# Change the permissions, to be executed
os.chmod(shortcutpath, posix.stat(shortcutpath).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
#TODO Find a way to make this change in Windows, so the shortcut can be executed in Linux

