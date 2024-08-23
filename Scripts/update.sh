
clear
echo "\033[1;36m updating..."
sleep 3
cd ..
rm -rf Clashrun
git clone 'https://github.com/Scriptmagum/ClashRun.git'
cd ClashRun
python3 Clashrun.py