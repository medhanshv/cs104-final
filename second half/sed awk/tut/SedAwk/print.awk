#This is print.awk
BEGIN{
FS=":"
OFS=";;;"
}
/run/ {
print $1, $4
}
