#!/bin/bash

sed -i 's/\r//g' check.awk

python3 script.py

rm output.txt
