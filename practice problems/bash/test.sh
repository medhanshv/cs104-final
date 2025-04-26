file=$1

while read -r line; do
    arr=($line)
    for((i=0;i<${#arr[@]};i++)); do
        echo "${arr[i]}"
    done
done <"$file"