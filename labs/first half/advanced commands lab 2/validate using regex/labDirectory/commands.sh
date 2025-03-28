# Write your commands here
# run with 'bash commands.sh' 
grep -E "[a-z]+[0-9]{2} [1-4] (22|23)b[0-9]{4}@iitb\.ac\.in submission.sh$" collect.txt > valid.txt
cut valid.txt -d ' ' -f 1,3|cut -d '@' -f 1|sort -t ' ' -n -k 2.4 > sorted.txt 
