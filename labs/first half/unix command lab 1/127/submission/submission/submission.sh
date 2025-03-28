mkdir outputs
cp `find inputs/ -type f -iname "*.txt"` outputs/
cat -n `find outputs/ -type f -iname "*.txt"|sort` > cat.txt
cat `find outputs/ -type f -iname "*.txt"` | grep -cv "^$" >lines.txt