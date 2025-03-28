#!/bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"

ptcd=$(pwd)
# INSTRUCTOR_SCRIPTS="${ptcd}/.evaluationScripts"
# LAB_DIRECTORY="${ptcd}/labDirectory"

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

# list_of_files="$(ls $LAB_DIRECTORY)"

cp ${LAB_DIRECTORY}/check.awk autograder/

cd ./autograder/

# chmod -R 777 $list_of_files

bash grader.sh

rm check.awk
# cd "$ptcd"