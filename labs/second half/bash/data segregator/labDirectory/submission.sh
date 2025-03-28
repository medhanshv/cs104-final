#!/bin/bash
grader(){
    total=$(echo $1 | cut -d ',' -f 6)
    if [[ $total -gt 85 ]]; then
    echo -n "AA"
    elif [[ $total -gt 65 ]]; then
    echo -n "AB"
    elif [[ $total -gt 45 ]]; then
    echo -n "BB"
    elif [[ $total -gt 35 ]]; then
    echo -n "CC"
    else   
    echo -n "F"
    fi
}

Grades=$1
sed 's/\r/\n/g' "$Grades" > g1.csv
firstline=$(head -n 1 g1.csv)
firstline=${firstline},grades
echo ${firstline}>ug23.csv
echo ${firstline}>ug24.csv
tail -n +2 g1.csv > g2.csv
grades=g2.csv
while read -r line; do
    year=$(echo $line | cut -d ',' -f 1 | cut -d 'B' -f 1)
    grade=$(grader "$line")
    output=${line},${grade}
    if [[ $year -eq 24 ]]; then
    echo $output >> ug4.csv
    elif [[ $year -eq 23 ]]; then
    echo $output >> ug3.csv
    fi
done < "$grades"

sort -n -t ',' -k 1,4 ug3.csv | sort -t ',' -k 7 >> ug23.csv
sort -n -t ',' -k 1,4 ug4.csv | sort -t ',' -k 7 >> ug24.csv
rm g1.csv g2.csv ug3.csv ug4.csv