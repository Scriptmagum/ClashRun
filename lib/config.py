import os
import json
try:
    from colorama import Fore,Back,Style,init
except ModuleNotFoundError:
    os.system("pip install colorama")
    from colorama import Fore,Back,Style,init
init(autoreset=True)

B,_b=Fore.BLUE,Back.BLUE

R,r=Fore.RED,Back.RED

Y,y=Fore.YELLOW,Back.YELLOW

G,g=Fore.GREEN,Back.GREEN

W,w=Fore.WHITE,Back.WHITE

C,c=Fore.CYAN,Back.CYAN

B,b=Fore.BLACK,Back.BLACK

S=Style.BRIGHT

U="\033[4m"

reset= Style.RESET_ALL
with open("Assets/config.json","r") as file:
    config=json.load(file)
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
                                                                                                       
{C+S} version {config["version"]}
{W}@copyright {C+S}2024{W} by {C+S}{config["author"]}
{W}Visit us at {C+S}{config["github_author"]}
'''
platform=os.name
langs={"py":"python3","sh":"bash","js":"node","pl":"perl","rb":"ruby"}
def show_config():
    print()
    print(f"{W}{'_'*61}")
    print(f"{C+S}{'Keys'.center(30)}{W+S} {'Values'.center(30)}")
    print(f"{W}{'_'*61}")
    for key in config:
        if key not in ["init","site"]:
            print(f"{C+S if key in ['clash_time','editor','langage']else C}{key.center(30)}{W+S if key in ['clash_time','editor','langage'] else W} {config[key].center(30)}")
    print()
