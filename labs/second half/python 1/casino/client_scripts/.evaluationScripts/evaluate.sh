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

# chmod -R 777 $list_of_files

python3 script.py

rm -r main.py

cd "$ptcd"
