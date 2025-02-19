#! /bin/bash


INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"


ptcd=$(pwd)

# For Testing
# INSTRUCTOR_SCRIPTS="${ptcd}/.evaluationScripts"
# LAB_DIRECTORY="${ptcd}/labDirectory"


cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

list_of_files="$(ls $LAB_DIRECTORY)"


cp -r $LAB_DIRECTORY/submission.sh autograder/

cd ./autograder/

# chmod -R 777 $list_of_files

./grader.sh

rm submission.sh

# rm -r $list_of_files

cd "$ptcd"
