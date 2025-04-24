# arr=()
# for ((i=1; i<=$#; i++)); do
#     arr[i]=$i
# done

# # arr=("${@}")
# # len = $#
# len=${#arr[@]}
# echo ${arr[@]}



merge_sort(){
    echo "called merge sort" >> output.txt
    local arr=("${@}")
    local n=${#arr[@]}

    if [[ $n -eq 1 ]];then
        echo ${arr[@]}
        return
    fi

    if [[ $n -eq 2 ]];then
        if [[ ${arr[0]} -le ${arr[1]} ]];then
        echo "${arr[0]} ${arr[1]}"
        else 
        echo "${arr[1]} ${arr[0]}"
        fi
        return
    fi

    local half=$((n/2))
    local arr1=("${arr[@]:0:$half}")
    echo "arr1 is ${arr1[@]}" >> output.txt
    local arr2=("${arr[@]:$half}")
    echo "arr2 is ${arr2[@]}" >> output.txt
    local sorted1=($(merge_sort "${arr1[@]}"))
    echo "sort1 is ${sorted1[@]}" >> output.txt
    local sorted2=($(merge_sort "${arr2[@]}"))
    echo "sort2 is ${sorted2[@]}" >> output.txt

    merger "${#sorted1[@]}" "${sorted1[@]}" "${sorted2[@]}"

}


merger(){
    echo "called merge" >> output.txt
    local num=$1
    echo "num is $num" >> output.txt
    local arr1=("${@:2:num}")
    echo "arr1 for merging is ${arr1[@]}" >> output.txt
    local arr2=("${@:((num+2))}")
    echo "arr2 for merging is ${arr2[@]}" >> output.txt
    len1=${#arr1[@]}
    len2=${#arr2[@]}
    arr3=()
    local count=0
    local i=0
    local j=0
    while [[ $i -lt $len1 && $j -lt $len2 ]]; do
        if ((arr1[i]<arr2[j])); then
            arr3[count]=${arr1[i]}
            echo "appended ${arr1[i]}" >> output.txt
            ((count++))
            ((i++))
        elif ((arr1[i]==arr2[j])); then
            arr3[count]=${arr2[j]}
            echo "appended ${arr2[j]} twice" >> output.txt
            ((count++))
            arr3[count]=${arr1[i]}
            echo "appended ${arr1[i]} cuz less" >> output.txt
            ((count++))
            ((i++))
            ((j++))
        else
            arr3[count]=${arr2[j]}
            echo "appended ${arr2[j]} cuz less" >> output.txt
            ((count++))
            ((j++))
            fi
    done

        while ((i<len1)); do
            arr3[count]=${arr1[i]}
            echo "appended ${arr1[i]} last ka" >> output.txt
            ((count++))
            ((i++))
            done

        while ((j<len2)); do
            arr3[count]=${arr2[j]}
            echo "appended ${arr2[j]} last ka" >> output.txt
            ((count++))
            ((j++))
        done
    

    echo ${arr3[@]}
}

echo "starting w ${@}" > output.txt
merge_sort "${@}"