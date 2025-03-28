#!/bin/bash
mapfile=$1
while read -r line; do
  arr=($line)
  if [[ ${#arr[@]}==2 ]]; then
  file=$(find . -type f -iname "${arr[0]}.pdf")
  if [ -f "$file" ]; then
    newname=${arr[0]}_${arr[1]}.pdf
    mv $file $newname
  fi
  fi
done < "$mapfile"