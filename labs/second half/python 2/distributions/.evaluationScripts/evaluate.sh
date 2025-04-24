#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
# INSTRUCTOR_SCRIPTS="."
LAB_DIRECTORY="../labDirectory"


ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd


cp -r $LAB_DIRECTORY/main.py autograder/

cd ./autograder/

chmod 777 main.py
./grader.sh

rm -r main.py

cd "$ptcd"
