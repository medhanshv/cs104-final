#!/bin/bash

sed -i 's/\r//g' email.awk
sed -i 's/\r//g' email.sed

python3 script.py
