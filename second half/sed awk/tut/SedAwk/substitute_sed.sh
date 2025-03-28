echo "Virahanka found the Fibonacci Numbers first. Fibonaccu found them later." > try.txt
echo "Original text..."
cat try.txt
echo ""
echo ""
echo "Change the word at 2nd occurrence..."
echo "sed 's/Fibonacci/Pythagoras/2' try.txt"
sed 's/Fibonacci/Pythagoras/2' try.txt
echo ""
echo ""
echo "Change the word at ALL occurrences..."
echo "sed 's/Fibonacci/Pythagoras/g' try.txt"
sed 's/Fibonacci/Pythagoras/g' try.txt
echo ""
echo ""
echo "Look at this parentheses problem..."
echo "This is normal regex..."
echo "echo '(Hi)' | sed 's/\(Hi\)/**/'"
echo '(Hi)' | sed 's/\(Hi\)/**/'
echo ""
echo ""
echo "This is EXTENDED regex..."
echo "echo '(Hi)' | sed -E 's/\(Hi\)/**/'"
echo '(Hi)' | sed -E 's/\(Hi\)/**/'

