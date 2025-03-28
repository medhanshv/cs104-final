#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"

cd $INSTRUCTOR_SCRIPTS

cp -r $LAB_DIRECTORY/working_directory.tar.gz autograder/

cd ./autograder/

chmod -R 777 working_directory.tar.gz
git config --global --add safe.directory /home/.evaluationScripts/autograder/working_directory

./grader.sh

rm -rf working_directory.tar.gz
