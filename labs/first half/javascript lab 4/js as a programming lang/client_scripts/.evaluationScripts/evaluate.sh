#!/bin/bash
cd /home/.evaluationScripts
cp /home/labDirectory/basic.html ./.autograder
cd .autograder
python3 script.py
rm basic.html