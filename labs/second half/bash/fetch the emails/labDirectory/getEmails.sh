
#!/bin/bash
if [[ $# -ne 1 ]]; then
    echo "Usage: ./getEmails.sh <file>"
    exit 1
fi

file="$1"  # Assign the first argument to the variable 'file'

# Check if file exists
if [[ ! -f $file ]]; then
    echo "Input File doesn't exist"
    exit 1
fi

cat $file |grep -E "[a-zA-Z0-9]*@[a-zA-Z]*.iitb.ac.in$">emails.txt
sort -rf emails.txt > sortedEmails.txt
cat sortedEmails.txt |grep -E "[a-zA-Z0-9]*@cse.iitb.ac.in$">cseEmails.txt
