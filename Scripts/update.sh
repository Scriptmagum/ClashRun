
clear
echo -e "\033[1;36m updating...\033[0m"
sleep 3
cd ..
rm -rf ClashRun
git clone 'https://github.com/Scriptmagum/ClashRun.git'
sleep 1.5
clean
cd ClashRun
python3 Clashrun.py