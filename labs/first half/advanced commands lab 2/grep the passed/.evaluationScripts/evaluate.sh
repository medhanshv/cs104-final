#! /bin/bash

# For Testing

INSTRUCTOR_SCRIPTS=$(pwd)"/.evaluationScripts"
LAB_DIRECTORY=$(pwd)"/labDirectory"

#Actual
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"


echo "INSTRUCTOR SCRIPTS: ${INSTRUCTOR_SCRIPTS}"
echo "LAB DIRECTORY: ${LAB_DIRECTORY}"

ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

list_of_files="submission.sh"

echo "Files: ${list_of_files}"


cp -r $LAB_DIRECTORY/submission.sh autograder/

cd ./autograder/

echo $(ls)
echo

chmod -R 777 $list_of_files

./grader.sh

rm -r $list_of_files

cd "$ptcd"