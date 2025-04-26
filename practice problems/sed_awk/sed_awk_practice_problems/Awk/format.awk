BEGIN{
    FS=" "
    OFS=";"
    code=""
    output=""
    report=""
}
NR==1{
    for(i=1; i<=NF ;i++){
        printf "%s;", $i
    }
    print "Comments"
}
NR==2{
    for(i=1; i<=NF ;i++){
        printf "%s;", $i
    }
    code=$2
    output=$3
    report=$4   
    print "-"
}
NR>2{
    check=1
    for(i=1; i<=NF ;i++){
        printf "%s;", $i
    }
    if($2 !~ /^[A-Za-z0-9_]+\.cpp$/){
        check=0
    }   
    else if($3 !~ /^[A-Za-z0-9_]+\.txt$/){
        check=0
    } 
    else if($4 !~ /^[A-Za-z0-9_]+\.pdf$/){
        check=0
    }
    if(check==1){
        print"Correct Submission Format"
    } 
    else{
        print "Wrong Submission Format"
    }
}