BEGIN{
    FS=",";
    OFS=",";
    ORS="\n";
}

NR==1{
    print $0,"Amount"
}
NR>1{
    if (match($2, /([0-9]+) (years)/, arr)){
        yrs=arr[1];
    }
    ans=($3)*pow(($5)^yrs)
    print $0,ans
}