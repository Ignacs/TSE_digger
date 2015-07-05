# -*- coding: big5 -*-
# test that how to call module_template.py 
import glob, os, sys, platform, subprocess
from os import listdir
from os.path import isfile, join

#import module_PriceAVG 
#import module_template

# python module_template.py  '/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'
# subprocess.call(['python', 'module_template.py', '/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'], shell=False)
# module_PriceAVG.module_func(['/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'])
#arg='/home/rox/lab/stock/TSE_dwrobot/db_test/0050.sl3'
#folder='/home/rox/lab/git_test/TSE_robot/TSE_dwrobot'
# folder='/home/ignacs/lab/git_test/TSE_robot/TSE_dwrobot'

############# function to get paht of all files under folder #############
def get_filepaths(directory, subname):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.
    print("Handle " + str(directory) + "...")

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths  # Self-explanatory.

############# function to list all files #############
def list_files(path):
    ''' function to list all files under some path
            '''
    # returns a list of names (with extension, without full path) of all files 
    # in folder path
    files = []
    for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)):
                    files.append(name)
    return files 


################################################################################
################################  main section  ################################

#for foundFiles in list_files(folder):
#	print (foundFiles)


# Run the above function and store its results in a variable.   
# for foundFiles in get_filepaths(folder):
#	print (foundFiles)


# func can filter subname
# Recursively find all *.sh files in **/usr/bin**
# sh_files_pattern = Match(filetype='f', name=dbFile_filter)

# sys.exit()
