#!/usr/bin/env python3
# move_jpegs_with_rename.py
# ARCHIVED.
# "Perfectly dumb" due to hardcoding + buggy implementation.
#
# Moved jpgs from hardcoded /sourcedir/jpeg to /targetdir/ with naive
# collision renaming. The rename logic on first collision produces
# "name-.ext" instead of "name-1.ext".
#
# Trivial task better solved with coreutils or a 5-line script using
# proper destination handling.
#
# Originally: messy_area/moveFilesWithAutoRename.py

import os

os.chdir('/sourcedir/jpeg')


targetDir = '/targetdir/'

def moveFileWithAutoRename(pathToFile,dstDir):
    basename = os.path.basename(pathToFile)
    dstFile = os.path.join(dstDir, basename)
    if os.path.exists(dstFile):
       basename = os.path.splitext(basename)[0] + '-' + os.path.splitext(basename)[1]   
    count = 1
    while os.path.exists(dstFile):
            newbasename = os.path.splitext(basename)[0] + str(count) + os.path.splitext(basename)[1]
            count += 1
            dstFile = os.path.join(dstDir,newbasename)
    print('moving ' + pathToFile + dstFile)
    os.rename(pathToFile,dstFile)    

fileList = os.listdir()

for file in fileList:
    if file.endswith(('.jpg','.jpeg')):
        moveFileWithAutoRename('./'+file, targetDir)
