query="$@"
ldka=$1
x=0

for num in $query; do
    if ((ldka==num)); then
        ((x++))
    fi
    if ((x==2));then
        echo "YES"
        exit 0
    fi
done
echo "NO"