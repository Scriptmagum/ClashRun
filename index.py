import re
import json
import os
import sys
import random
from config import *
from clash import Clash

help=f"""
{G+S}
list of command:

Clash: to start an instance of clash

help: to display the help

config: display config key value

set: change  config key value

solution: view the precedent clash solution

quit: end the game
"""


def main():
    if config["init"]:
        os.system("bash Scripts/install.sh")
        InitClash=Clash()
        InitClash.fetch_clashes()
        config["init"]=(7==5) #lol
        with open("Scripts/config.json","r") as f:
            f.write(json.dumps(config,indent=2))
        del InitClash

# Display the banner of scriptclash 
    print(banner)
    reg_play=r"^clash\s+(fastest|shortest|reverse|f|r|s)\s*$|^clash\s*$"
    reg_quit=r"^(quit|q)\s*$"
    reg_help=r"^(help|h)\s*$"
    reg_sol=r"^(solution|sol)\s*$"

    while True:
        try:
            read=input(f"{Y}<\\>{reset}{W}")
            match_clash=re.search(reg_play,read,re.IGNORECASE)
            match_quit=re.search(reg_quit,read,re.IGNORECASE)
            match_help=re.search(reg_help,read,re.IGNORECASE)
            match_sol=re.search(reg_sol,read,re.IGNORECASE)
            if match_clash:
                mode=match_clash.group(1).lower() if match_clash.group(1) else random.choice(["fastest","shortest","reverse"])
                mode="fastest"if mode=='f' else "reverse"if mode=='r' else "shortest" if mode=='s' else mode
                clash=Clash(mode)
                clash.begin()
            elif match_help:
                print(help)
            elif match_sol:
                try:
                    print(f"{W+S}lang: {G+S}{clash.solution_lang}")
                    print(clash.solution)
                except:
                    print(f"{R}clash solution not found. play one clash before")
            elif match_quit:
                
               quit()
        except KeyboardInterrupt:
            raise Exception("keybord interrupt")
if __name__=="__main__":
    main()
