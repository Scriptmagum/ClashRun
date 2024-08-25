import os
import sys
import time
import json
try:
    from colorama import Fore,Back,Style,init
except ModuleNotFoundError:
    os.system("pip install colorama ")
    from colorama import Fore,Back,Style,init
init()

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
platform=os.name
langs={"py":"python3","sh":"bash","js":"node","pl":"perl","rb":"ruby"}
with open("Assets/config.json","r") as file:
    config=json.load(file)

help=f"""{W+S+U}
list of commands:

{reset+Y+U}clash:{reset+W} to start an instance of clash
usage: clash [ < ( reverse | r )| ( fastest | f ) | ( shortest | s ) > ];simple clash will choose
either reverse,either fastest,or shortest 

{Y+U}help:{reset+W}  to display the help

{Y+U}set:{reset+W}  change  configuration value,or display it
usage: set [<key:value>];simple set will display configuration key,value

{Y+U}solution:{reset+W}  view the precedent clash solution
usage: solution|sol

{Y+U}update:{reset+W}  use it to get the last version of ClashRun

{Y+U}quit:{reset+W}  quit the game
"""
help_clash=f"""{W+S+U}
list of commands:

{reset+Y+U}run:{reset+W} to run and check if your solution is correct
usage: run | r

{Y+U}open:{reset+W} to open an editor
usage: open [<py | rb | js | pl | sh> ]; use to open either python,ruby,javascript,perl or bash file
or simple use, open ,then it will open your default langage

{Y+U}pass:{reset+W}  pass to another clash
usage: pass

{Y+U}char:{reset+W}  display current numbers of charcaters if mode is shortest
usage: char

{Y+U}time:{reset+W} display the remaining time before clash finish
usage: time | t

{Y+U}help:{reset+W}  display help
usage: help | h
"""
banner = fr'''{Y}

 ▄████▄   ██▓    ▄▄▄        ██████  ██░ ██  ██▀███  
▒██▀ ▀█  ▓██▒   ▒████▄    ▒██    ▒ ▓██░ ██▒▓██ ▒ ██▒
▒▓█    ▄ ▒██░   ▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒██░   ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒██▀▀█▄  
▒ ▓███▀ ░░██████▒▓█   ▓██▒▒██████▒▒░▓█▒░██▓░██▓ ▒██▒
░ ░▒ ▒  ░░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒▓ ░▒▓░
  ░  ▒   ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ░▒ ░ ▒░
░          ░ ░    ░   ▒   ░  ░  ░   ░  ░░ ░  ░░   ░ 
░ ░          ░  ░     ░  ░      ░   ░  ░  ░   ░     
░{reset+W}'''                                                   
                                                                                                                                                                                                                                                                                            

banner_text=f'''{C+S}version {config["version"]}
{W}@copyright {C+S}2024{W} by {C+S}{config["author"]}
{W}Visit us at {C+S}{config["github_author"]}
'''
def print_slow(text,delay=0.05):
        for char in text:sys.stdout.write(char);sys.stdout.flush();time.sleep(delay)
        print(f"{reset+W}")
def show_config():
    print()
    print(f"{W}{'_'*61}{reset+W}")
    print(f"{C+S}{'Keys'.center(30)}{W+S} {'Values'.center(30)}{reset+W}")
    print(f"{W}{'_'*61}{reset+W}")
    for key in config:
        if key not in ["init","site"]:
            print(f"{C+S if key in ['clash_time','editor','langage','limit_characters']else C}{key.center(30)}{W+S if key in ['clash_time','editor','langage','limit_characters'] else W} {config[key].center(30)}{reset+W}")
    print()
