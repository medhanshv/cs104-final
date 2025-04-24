mapfile lines < jsp.txt
for el in ${lines[@]}; do
    echo "$el"
done