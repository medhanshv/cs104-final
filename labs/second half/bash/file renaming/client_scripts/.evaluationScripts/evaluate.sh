#!/bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"

cd $INSTRUCTOR_SCRIPTS

list_of_files="$(ls $LAB_DIRECTORY)"

cp -r $LAB_DIRECTORY/* autograder/

cd ./autograder/

chmod -R 777 $list_of_files

bash grader.sh

rm -r $list_of_files
