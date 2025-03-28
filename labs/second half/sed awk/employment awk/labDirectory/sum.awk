BEGIN{ 
FS=","
}
{
    print $0
}
NR > 1{
    net+=$4
    if($3=="Film"){
        film+=$4
    }
    if($3=="Agriculture"){
        agr+=$4
    }
    if($3=="Banking"){
        bank+=$4
    }
    if($3=="Manufacturing"){
        manu+=$4
    }
    if($3=="Railways"){
        rail+=$4
    }
}
END{
    print"====="
    print "Net : " net
    print "Agriculture : " agr
    print "Banking : " bank
    print "Film : " film
    print "Manufacturing : " manu
    print "Railways : " rail

 }