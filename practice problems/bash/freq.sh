# declare -A letter
file=$1

# checker(){
#     local word=$1
#     ((letter["${word}"]++))
# }

# while read -r line; do
#     arr=($line)
#     for word in ${arr[@]}; do
#         checker $word
#     done
# done <"$file"

while read -r line; do
    arr=($line)
    length=${#arr[@]}
    for ((i=0;i<length;i++)); do
        echo "${arr[$i]}"
    done
done <"$file"

# for word in ${!letter[@]}; do
#     echo "$word : ${letter["$word"]}"
# done