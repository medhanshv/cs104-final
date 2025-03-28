echo "Hi John Watson" > try.txt
echo "Hi Mary" >> try.txt
echo "Hi Sherlock Holmes" >> try.txt
echo "Hi Mycroft Holmes" >> try.txt
echo "Hi Hudson" >> try.txt
echo "Hi Molly" >> try.txt
echo "cat try.txt"
cat try.txt
echo ""
echo ""
echo "Only p, no -n..."
echo "sed '/Holmes/ s/Hi/Bye/p' try.txt"
sed '/Holmes/ s/Hi/Bye/p' try.txt
echo ""
echo ""
echo "p with -n..."
echo "sed -n '/Holmes/ s/Hi/Bye/p' try.txt"
sed -n '/Holmes/ s/Hi/Bye/p' try.txt
echo ""
echo ""
echo "Only -n, no p..."
echo "sed -n '/Holmes/ s/Hi/Bye/' try.txt"
sed -n '/Holmes/ s/Hi/Bye/' try.txt
echo ""
echo ""
echo "Delete d command..."
echo "sed '/Holmes/d' try/txt"
sed '/Holmes/d' try.txt
echo ""
echo ""
echo "Append a ..."
echo "sed '/Sherlock/a Hello Irene Adler' try.txt"
sed '/Sherlock/a Hello Irene Adler' try.txt
echo ""
echo ""
echo "Insert i ..."
echo "sed '/Sherlock/i Hello Irene Adler' try.txt"
sed '/Sherlock/i Hello Irene Adler' try.txt
echo ""
echo ""
echo "Replace c ..."
echo "sed '/Sherlock/c Die James Moriarty' try.txt"
sed '/Sherlock/c Die James Moriarty' try.txt
echo ""
echo ""
echo "Quit q..."
echo "sed '/Sherlock/q' try.txt"
sed '/Sherlock/q' try.txt
