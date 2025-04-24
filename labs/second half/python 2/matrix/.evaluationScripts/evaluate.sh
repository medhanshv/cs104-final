#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
# INSTRUCTOR_SCRIPTS="."
LAB_DIRECTORY="../labDirectory"


ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

# list_of_files="$(ls $LAB_DIRECTORY)"


cp -r $LAB_DIRECTORY/main.py autograder/

cd ./autograder/

chmod 777 main.py

./grader.sh

rm -rf main.py

cd "$ptcd"
