BEGIN{
# Remember to use "" here not ''
FS=":"
OFS="\t"
print "Beginning..."
}
/run/ {
print $1, $4
}
END{
print "Done!"
}
