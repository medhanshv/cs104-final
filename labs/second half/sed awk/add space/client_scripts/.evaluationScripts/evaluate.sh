#! /bin/bash

# Actual

INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"

# Testing 

ptcd=$(pwd)

# INSTRUCTOR_SCRIPTS="${ptcd}/.evaluationScripts"
# LAB_DIRECTORY="${ptcd}/labDirectory"

# echo "INSTRUCTOR SCRIPTS: ${INSTRUCTOR_SCRIPTS}"
# echo "LAB DIRECTORY: ${LAB_DIRECTORY}"
# echo $ptcd


cd $INSTRUCTOR_SCRIPTS

# echo "Files: ${list_of_files}"

cp -r $LAB_DIRECTORY/add_space.sed autograder/

cd ./autograder/
ls

# echo $(ls)

bash grader.sh

cd ..
rm -r autograder/add_space.sed

cat evaluate.json


cd "$ptcd"

