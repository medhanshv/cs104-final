#!/bin/bash
cd /home/.evaluationScripts
cp /home/labDirectory/script.html ./.autograder
cd .autograder
python3 script.py
rm script.html