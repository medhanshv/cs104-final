#This is printf.awk
BEGIN{
FS=":"
OFS=";;;"
}
/run/ {
printf "%s----%s\n", $1, $4
}
