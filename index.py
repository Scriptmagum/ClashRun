import re
import json
import os
import sys
import random
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
from colorama import Fore,Back,Style,init
from utils import Clash

init(autoreset=True)

B=Fore.BLUE

R=Fore.RED

Y=Fore.YELLOW

G=Fore.GREEN

W=Fore.WHITE

C=Fore.CYAN

S=Style.BRIGHT

with open("config.json","r") as file:
    config=json.load(file)

"""
list of command:

Clash: to start an instance of clash

help: to display the help

config: display config key value

set: change  config key value

quit: end the game

run: test your clash

"""
mode_clash="fastest"

reg_play=r"^clash\s+(fastest|shortest|reverse|f|r|s)\s*$|^clash\s*$"
reg_quit=r"^(quit|q)\s*$"


banner = f'''{Y}
                                                                                                                                                                                                            
  ,----..     ,--,                                 ,---,       ,-.----.                                
 /   /   \  ,--.'|                               ,--.' |       \    /  \                               
|   :     : |  | :                               |  |  :       ;   :    \           ,--,        ,---,  
.   |  ;. / :  : '                    .--.--.    :  :  :       |   | .\ :         ,'_ /|    ,-+-. /  | 
.   ; /--`  |  ' |       ,--.--.     /  /    '   :  |  |,--.   .   : |: |    .--. |  | :   ,--.'|'   | 
;   | ;     '  | |      /       \   |  :  /`./   |  :  '   |   |   |  \ :  ,'_ /| :  . |  |   |  ,"' | 
|   : |     |  | :     .--.  .-. |  |  :  ;_     |  |   /' :   |   : .  /  |  ' | |  . .  |   | /  | | 
.   | '___  '  : |__    \__\/: . .   \  \    `.  '  :  | | |   ;   | |  \  |  | ' |  | |  |   | |  | | 
'   ; : .'| |  | '.'|   ," .--.; |    `----.   \ |  |  ' | :   |   | ;\  \ :  | : ;  ; |  |   | |  |/  
'   | '/  : ;  :    ;  /  /  ,.  |   /  /`--'  / |  :  :_:,'   :   ' | \.' '  :  `--'   \ |   | |--'   
|   :    /  |  ,   /  ;  :   .'   \ '--'.     /  |  | ,'       :   : :-'   :  ,      .-./ |   |/       
 \   \ .'    ---`-'   |  ,     .-./   `--'---'   `--''         |   |.'      `--`----'     '---'        
  `---`                `--`---'                                `---'                                   
                                                                                                       
{C+S} version 1.0
{W}@copyright {C+S}2024{W} by {C+S}zh3_gh05t
{W}Visit us at {C+S}https://github.com/Scriptmagum
'''
def main():

# Display the banner of scriptclash 
    print(banner)

    while True:
        try:
            read=input(f"{W}>")

            match_clash=re.search(reg_play,read,re.IGNORECASE)
            match_quit=re.search(reg_quit,read,re.IGNORECASE)

            if match_clash:
                mode=match_clash.group(1).lower() if match_clash.group(1) else random.choice(["fastest","shortest","reverse"])
                mode="fastest"if mode=='f' else "reverse"if mode=='r' else "shortest" if mode=='s' else mode
                clash=Clash(mode,config)
                clash.begin()

            elif match_quit:
               quit()






        except KeyboardInterrupt:
            raise Exception("keybord interrupt")









if __name__=="__main__":
    main()
