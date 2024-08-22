check(){
command -v "$1" >/dev/null 2>&1
}
intall(){
    if ! check $1;then
    sudo apt install $2
    fi
}
install "python3" "python3";install "ruby" "ruby";install "node" "nodejs";install "perl" "perl"
