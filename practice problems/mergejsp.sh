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
    echo "half is $half arr[0] is ${arr[0]} & arr[half?!] is ${arr[$half]}" >> output.txt
    local arr1=("${arr[@]:0:$half}")
    echo "arr1 is ${arr1[@]}" >> output.txt
    local arr2=("${arr[@]:$half}")
    echo "arr2 is ${arr2[@]}" >> output.txt
    local sorted1=($(merge_sort "${arr1[@]}"))
    echo "sort1 is ${sorted1[@]}" >> output.txt
    local sorted2=($(merge_sort "${arr2[@]}"))
    echo "sort2 is ${sorted2[@]}" >> output.txt

    merge "${#sorted1[@]}" "${sorted1[@]}" "${sorted2[@]}"

}

merge(){
    echo "called merge" >> output.txt
    local num=$1
    echo "num is $num" >> output.txt
    local arr1=("${@:2:num}")
    echo "arr1 for merging is ${arr1[@]}" >> output.txt
    local arr2=("${@:((num+2))}")
    echo "arr2 for merging is ${arr2[@]}" >> output.txt
    local len1=${#arr1[@]}
    local len2=${#arr2[@]}
    echo "len1 $len1 len2 $len2" >> output.txt
    local j=0
    local k=0
    local merged=()

    while ((j<len1 && k<len2));do
        if [[ ${arr1[j]} -eq ${arr2[k]} ]]; then
            merged[j+k]="${arr1[j]}"
            echo "appended ${arr1[j]}" >> output.txt
            ((j++))
            merged[j+k]="${arr2[k]}"
            echo "appended ${arr2[k]}" >> output.txt
            ((k++))

        elif [[ ${arr1[j]} -lt ${arr2[k]} ]];then
            merged[j+k]="${arr1[j]}"
            echo "appended ${arr1[j]}" >> output.txt
            ((j++))
        else
            merged[j+k]="${arr2[k]}"
            echo "appended ${arr2[k]}" >> output.txt
            ((k++))
        fi
    done
    
    if ((j>=len1));then
        while ((k<len2));do
            merged[j+k]="${arr2[k]}"
            echo "appended ${arr2[k]}" >> output.txt
            ((k++))
        done
    fi
    if((k>=len2)); then
        while ((j<len1));do
            merged[j+k]="${arr1[j]}"
            echo "appended ${arr1[j]}" >> output.txt
            ((j++))
        done
    fi

    echo ${merged[@]}
}


given=("${@}")
echo "starting with ${@}" > output.txt
merge_sort "${given[@]}"