#!bin/bash
swap(){
    temp=${arr[$1]}
    arr[$1]=${arr[$2]}
    arr[$2]=$temp
}

max_to_end(){
    local idx=$1
    local max=0
    for((j=0;j<=idx;j++)); do
        if ((arr[j]>arr[max])); then
            max=$j
        fi
    done
    swap "$max" "$idx"
}

arr=($@)

for ((i=$#-1; i>=1; i--)); do
    max_to_end "$i"
done

echo "${arr[@]}"