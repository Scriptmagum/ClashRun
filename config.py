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
                                                                                                       
{C+S} version 1.0
{W}@copyright {C+S}2024{W} by {C+S}zh3_gh05t
{W}Visit us at {C+S}https://github.com/Scriptmagum
'''
platform=os.name

langs={"py":"python3","sh":"bash","js":"node","pl":"perl","rb":"ruby"}