echo "John Hi" > try.txt
echo "Sherlock Hi" >> try.txt
echo "Hi Sherlock" >> try.txt
echo "Hi John" >> try.txt
echo "This is try.txt..."
cat try.txt
echo ""
echo ""
echo "This is address via PATTERN..."
echo "sed '/Sherlock/ s/Hi/Bye/' try.txt"
sed '/Sherlock/ s/Hi/Bye/' try.txt
echo ""
echo ""
echo "This is address via LINE NUMBER..."
echo "sed '2,4 s/Hi/Bye/' try.txt"
sed '2,4 s/Hi/Bye/' try.txt
