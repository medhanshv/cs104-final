#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"


ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

list_of_files="$(ls $LAB_DIRECTORY)"


cp -r $LAB_DIRECTORY/getEmails.sh autograder/

cd ./autograder/

chmod -R 777 getEmails.sh

./grader.sh

rm -rf autograder/getEmails.sh

cd "$ptcd"
