#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"
EVAL_DIRECTORY="/home/.evaluationScripts/autograder/evalDirectory"
# INSTRUCTOR_SCRIPTS="/home/aria/Desktop/CS108/Midsem/.evaluationScripts"
# LAB_DIRECTORY="/home/aria/Desktop/CS108/Midsem/labDirectory"
# EVAL_DIRECTORY="/home/aria/Desktop/CS108/Midsem/.evaluationScripts/autograder/evalDirectory"

# ls -a
ptcd=$(pwd)
echo $ptcd

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd
pwd

cd ./autograder
cp -r evalDirectory/ evalDirectory2/

cp $LAB_DIRECTORY/Makefile $EVAL_DIRECTORY/Makefile
ls -a
cd evalDirectory
chmod 777 Makefile

if python3 script.py; then
    echo ""
else
    echo ""
    # Handle the failure gracefully or just continue with the script
fi

cd "$ptcd"

rm -rf $EVAL_DIRECTORY
mv $INSTRUCTOR_SCRIPTS/autograder/evalDirectory2 $EVAL_DIRECTORY

# rm -f $INSTRUCTOR_SCRIPTS/autograder/evaluate.json
