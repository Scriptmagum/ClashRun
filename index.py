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

# initializing of global variable

init(autoreset=True)

B,_b=Fore.BLUE,Back.BLUE

R,r=Fore.RED,Back.RED

Y,y=Fore.YELLOW,Back.YELLOW

G,g=Fore.GREEN,Back.GREEN

W,w=Fore.WHITE,Back.WHITE

C,c=Fore.CYAN,Back.CYAN

B,b=Fore.BLACK,Back.BLACK

S=Style.BRIGHT

with open("Script/config.json","r") as file:
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

banner = fr'''{Y}
                                                                                                                                                                                                            
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
    if config["init"]:
        InitClash=Clash(config)
        InitClash.fetch_clashes()
        config["init"]=(7==5) #lol
        with open("Script/config.json","w",encoding="utf-8") as file:
            file.write(json.dumps(config,indent=2))
        del InitClash

# Display the banner of scriptclash 
    print(banner)
    reg_play=r"^clash\s+(fastest|shortest|reverse|f|r|s)\s*$|^clash\s*$"
    reg_quit=r"^(quit|q)\s*$"
    while True:
        try:
            read=input(f"{W}>")
            match_clash=re.search(reg_play,read,re.IGNORECASE)
            match_quit=re.search(reg_quit,read,re.IGNORECASE)
            if match_clash:
                mode=match_clash.group(1).lower() if match_clash.group(1) else random.choice(["fastest","shortest","reverse"])
                mode="fastest"if mode=='f' else "reverse"if mode=='r' else "shortest" if mode=='s' else mode
                clash=Clash(config,mode)
                clash.begin()
            elif match_quit:
               quit()
        except KeyboardInterrupt:
            raise Exception("keybord interrupt")
if __name__=="__main__":
    main()
