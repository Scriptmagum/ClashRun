C="\033[1;36m"
W="\033[1;37m"
G="\033[1;32m"
check(){
command -v "$1" >/dev/null 2>&1
}
install(){
    if ! check "$1";then
        echo "$C installing $1..."
        sleep 2;sudo apt install -y "$2"
        if ! check "$1";then
        echo "try sudo apt  update before.."
        exit
        fi
    
    fi
    echo -e "$C $1 $W[$G OK $W]"  
    sleep 2
}
echo -e "$C installing  dependencing..."
wait 2
install "python3" "python3";install "ruby" "ruby";install "node" "nodejs";install "perl" "perl";install "bash" "bash"
