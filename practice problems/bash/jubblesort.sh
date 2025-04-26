((last=$#-1))
arr=("${@}")
while ((last>0)); do
    for ((i=0; i<$last; i++)); do
        if ((arr[i]>arr[i+1])); then
            tmp=${arr[i+1]}
            arr[i+1]=${arr[i]}
            arr[i]=$tmp
        fi
    done
    ((last--))
done
echo "${arr[@]}"