
sed 's/\r//g' commands.sh > temp
mv temp submission.sh


echo RUNNING script.py
python3 script.py

if [ -e "submission.sh" ] ; then
	rm submission.sh
fi 
