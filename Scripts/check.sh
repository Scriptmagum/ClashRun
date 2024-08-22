C="\033[1;36m"
W="\033[1;37m"
G="\033[1;32m"
R="\033[1;31m"

check(){
if command -v "$1" >/dev/null 2>&1;then
echo -e "$C $1 $G found $W[$G+$W]"
else
echo -e "$C $1 $R not found $W[$R-$W]"

fi
sleep 2
}
echo -e "$C checking dependencies..."
sleep 2
check "python3" ;check "ruby";check "node" ;check "perl" ;check "bash" 
