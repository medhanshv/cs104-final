#!/bin/bash

tail -n +2 $1 > tmp.csv
echo "rollno,quiz1,quiz2,midsem,endsem,total-marks,grades" > ug23.csv
echo "rollno,quiz1,quiz2,midsem,endsem,total-marks,grades" > ug24.csv

awk 'BEGIN{
        FS=",";
        OFS=",";
    }
{
marks=substr($6,1,length($6)-1)
if (marks > 85) { grade="AA";}
else if (marks  > 65) { grade="AB";}
else if (marks > 45) { grade="BB";}
else if (marks > 35) { grade="CC";}
else { grade="F";}
len=length($0)
line=substr($0,1,len-1)

}
/24B[0-9]*/{
print line,grade >> "ug4.csv"
}
/23B[0-9]*/{
print line,grade >> "ug3.csv"
}' tmp.csv


sort -n -t ',' -k 1 ug4.csv | sort -t ',' -k 7 >> ug24.csv
sort -n -t ',' -k 1 ug3.csv | sort -t ',' -k 7 >> ug23.csv

rm ug3.csv ug4.csv tmp.csv