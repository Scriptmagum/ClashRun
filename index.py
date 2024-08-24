import re
import json
import os
import sys
import random
from config import *
from clash import Clash
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
    os.system("clear")
    print(banner)
    print_slow(banner_text)
    reg_clash=r"^\s*clash\s+(fastest|shortest|reverse|f|r|s)\s*$|^\s*clash\s*$"
    reg_quit=r"^s*(quit|q)\s*$"
    reg_help=r"^\s*(help|h)\s*$"
    reg_sol=r"^\s*(solution|sol)\s*$"
    reg_set=r"^\s*set\s*$|^\s*set\s+(\w+)\s*:\s*(\w+)\s*$"
    reg_up=r"^\s*update\s*$"
    while True:
        try:
            read=input(f"{Y}<\\>{reset}{W}")
            match_clash=re.search(reg_clash,read,re.IGNORECASE)
            match_quit=re.search(reg_quit,read,re.IGNORECASE)
            match_help=re.search(reg_help,read,re.IGNORECASE)
            match_sol=re.search(reg_sol,read,re.IGNORECASE)
            match_set=re.search(reg_set,read,re.IGNORECASE)
            match_up=re.search(reg_up,read,re.IGNORECASE)
            if match_clash:
                mode=match_clash.group(1).lower() if match_clash.group(1) else random.choice(["fastest","shortest","reverse"])
                mode="fastest"if mode=='f' else "reverse"if mode=='r' else "shortest" if mode=='s' else mode
                clash=Clash(mode)
                clash.begin()
            elif match_help:
                print(help)
            elif match_sol:
                try:
                    print(f"{W+S}lang: {G+S}{clash.solution_lang}{reset+W}")
                    print(f"{W}{clash.solution}{reset+W}")
                except:
                    print(f"{R}clash solution not found. play one clash before{reset+W}")
            elif match_set:
                if match_set.group().strip().lower()=="set":
                    show_config()
                else:
                    key=match_set.group(1).lower()
                    value=match_set.group(2)
                    if key in config:
                        if key in ['clash_time','editor','langage']:
                            if key=='clash_time':
                                if re.search(r"^\d{2}$",value):
                                    config[key]=value
                                    print(f"\n{C}{key} {W}set to {value}{reset+W}\n")
                                else:print(f"{R}format must be in xx minutes{reset+W}")
                            elif key=="langage":
                                if value not in langs:
                                    print(f"\n{W}possibles langages:{G}{'; '.join(langs.keys())}{reset+W}\n")
                                else:
                                    config[key]=value.lower()
                                    print(f"\n{C}{key} {W}set to {value}\n{reset+W}")
                            else:
                                config[key]=value
                                print(f"\n{C}{key} {W}set to {value}{reset+W}\n")
                            with open("Assets/config.json","w") as f:
                                f.write(json.dumps(config,indent=2))
                        else:print(f"{R}impossible to modify {key}{reset+W}")
                    else:
                        print(f"{R}key not found XXX{reset+W}")
            elif match_up:
                os.system("bash Scripts/update.sh")
                quit()
            elif match_quit:quit()
            else:
                print(f"\n{W}try to see: {Y+S}help {W}please{reset+W}\n")
        except KeyboardInterrupt:
            raise Exception("keybord interrupt")
if __name__=="__main__":
    main()
