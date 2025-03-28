echo "$(dirname "$0")"
echo "$0"  #this tells u relative location of script wrt where script was executed
cd bash
echo "you are at $(pwd)"
echo "the script is at $0"
echo "you are at $(pwd)"
cd "$(dirname "$0")"
echo "you are at $(pwd)"
cd demo
echo "you are at $(pwd)"