BEGIN{
    FS=","
    OFS="\t"
}
NR==1{
    for(i=1; i<=NF ;i++){
    printf "%s\t", $i
    }
    printf "Average\n"
}
NR>1{
    for(i=1; i<=NF ;i++){
    printf "%s\t", $i
    }
    for(i=2; i<=NF ;i++){
    sum+=$i
    }
    avg = sum/(NF-1)
    print avg
    sum=0
}