#!/bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"

# ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

# list_of_files="$(ls $LAB_DIRECTORY)"

cp ${LAB_DIRECTORY}/var_change.sed autograder/

cd ./autograder/

# chmod -R 777 $list_of_files

# ./grader.sh

python3 script.py

rm var_change.sed

# cd "$ptcd"