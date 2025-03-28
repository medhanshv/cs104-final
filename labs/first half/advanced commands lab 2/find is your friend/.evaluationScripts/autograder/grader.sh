echo "Creating Testcase"
for ((i=1;i<=10;i++)); do
	./create.sh
done

echo "Done Creating Testcase"

tar -cf files.tar.gz bigdirectory/ >/dev/null 2>/dev/null
cp files.tar.gz files_backup.tar.gz

echo "Done creating tar file"

sed 's/\r//g' submission.sh > temp
mv temp submission.sh

python3 ./script.py

rm -rf bigdirectory files.tar.gz files_backup.tar.gz
rm -rf bigdirectory
