function printer(arr) {
    first = 1
    counter=0
    for (i in arr) {
        if (!first) printf " "
        printf "%d", arr[i]
        first = 0
        counter++
    }
    print ""
    if(counter>BUF_SIZE)check=0
}

function deleter(arr,n){
    for(i in arr){
        if(arr[i]==n){
            delete arr[i]
        }
    }
}

BEGIN{
    FS=" "
    count=0
    check=1
}

{
    if($1=="Produced"){
        arr[count++]=$2
    }
    if($1=="Consumed"){
        deleter(arr,$2)
    }
    printer(arr)
}

{
    if($3=="exiting"){
        if($1=="Master"){
            exitm[$2]+=1
        }
        else{
            exitw[$2]+=1
        }
        if(exitm[$2]>1||exitw[$2]>1)check=0
    }
    if($4=="master"){
        if($5>=NUM_MAS)check=0
        if($2>=TOTAL)check=0
        if(exitm[$5]==1)check=0
        else {produce[$2]+=1; global[$2]+=1}
        if(produce[$2]>1||produce[$2]<0)check=0
    }
    if($4=="worker"){
        if($5>=NUM_WOR)check=0
        if($2>=TOTAL)check=0
        if(exitw[$5]==1)check=0
        else {produce[$2]-=1; globale[$2]+=1}
        if(produce[$2]>1||produce[$2]<0)check=0
    }
    
}

END{
    for(i=0;i<TOTAL;i++){
        if(global[i]!=1)check=0
        if(globale[i]!=1)check=0
    }

    if(check==1)print "YES"
    else print "NO"
}

