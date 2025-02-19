#! /bin/bash

# For Testing
# INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
# LAB_DIRECTORY="/home/labDirectory"


# ptcd=$(pwd)

# cd $INSTRUCTOR_SCRIPTS
# # echo $ptcd

# list_of_files="$(ls $LAB_DIRECTORY)"


# cp -r $LAB_DIRECTORY/submission.sh autograder/
pip install bs4
cd /home/.evaluationScripts/autograder/

# chmod -R 777 $list_of_files

python3 script.py

# rm -r $list_of_files

cd "$ptcd"
