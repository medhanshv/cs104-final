mystring=$*
files=$(find . -type f -iname "*.out")
for file in $files; do
    echo $mystring >> $file
done
