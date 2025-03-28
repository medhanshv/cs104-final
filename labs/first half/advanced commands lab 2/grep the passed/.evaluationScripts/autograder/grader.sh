# bash submission.sh

sed 's/\r//g' submission.sh > temp
mv temp submission.sh

python3 script.py
