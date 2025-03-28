#!/bin/bash
pip install bs4
cd /home/.evaluationScripts
cp /home/labDirectory/dom.js ./.autograder
cd .autograder
python3 script.py
rm dom.js