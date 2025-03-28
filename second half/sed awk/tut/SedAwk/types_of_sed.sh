echo "This is inline sed..."
echo "sed s/Pythagoras/Fibonacci/g < input.txt"
sed s/Pythagoras/Fibonacci/g < input.txt
echo ""
echo ""
echo "Now this is sed via external file..."
echo "sed -f fibonacci.sed < input.txt"
sed -f fibonacci.sed < input.txt
