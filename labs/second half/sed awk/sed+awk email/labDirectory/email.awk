BEGIN{
    FS=","
}

NR==1{
    printf $0
    printf ",Email-ID\n"
}

NR>1{
    printf $0 "," $2 $4 "@surveycorps.com\n"
}