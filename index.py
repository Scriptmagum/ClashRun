import re
import json
import os
import sys
import random
from config import *
from clash import Clash

help=f"""{W+S}
list of commands:

clash: to start an instance of clash
usage: clash [<(reverse|r)|(fastest|f)|(shortest|s)>];simple clash will choose
either reverse,either fastest,or shortest 

help: to display the help

set: change  configuration value,or display it
usage: set [<key:value>];simple set will display configuration key,value

solution: view the precedent clash solution
usage: solution|sol

update: use it to get the last version of ClashRun

quit: quit the game
"""


def main():
    if config["init"]:
        os.system("bash Scripts/check.sh")
        InitClash=Clash()
        InitClash.fetch_clashes()
        config["init"]=(7==5) #lol
        with open("Assets/config.json","w") as f:
            f.write(json.dumps(config,indent=2))
        del InitClash

# Display the banner of scriptclash 
    print(banner)
    reg_clash=r"^clash\s+(fastest|shortest|reverse|f|r|s)\s*$|^clash\s*$"
    reg_quit=r"^(quit|q)\s*$"
    reg_help=r"^(help|h)\s*$"
    reg_sol=r"^(solution|sol)\s*$"
    reg_set=r"^set\s*$|set\s+\w+:\w+\s*$"

    while True:
        try:
            read=input(f"{Y}<\\>{reset}{W}")
            match_clash=re.search(reg_clash,read,re.IGNORECASE)
            match_quit=re.search(reg_quit,read,re.IGNORECASE)
            match_help=re.search(reg_help,read,re.IGNORECASE)
            match_sol=re.search(reg_sol,read,re.IGNORECASE)
            match_set=re.search(reg_set,read,re.IGNORECASE)
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
                    print(f"{W}{clash.solution}")
                except:
                    print(f"{R}clash solution not found. play one clash before")
            elif match_set:
                if match_set.group().strip().lower()=="set":
                    show_config()
                    
            elif match_quit:quit()
        except KeyboardInterrupt:
            raise Exception("keybord interrupt")
if __name__=="__main__":
    main()
