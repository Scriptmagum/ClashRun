import sys,os
import json
import re
import time
import random
import threading  # i love that ,fork process lol
try:
    import requests,colorama
except ModuleNotFoundError:
    os.system("pip install requests  colorama")
from colorama import Fore,Back,init,Style

init(autoreset=True)

B,_b=Fore.BLUE,Back.BLUE

R,r=Fore.RED,Back.RED

Y,y=Fore.YELLOW,Back.YELLOW

G,g=Fore.GREEN,Back.GREEN

W,w=Fore.WHITE,Back.WHITE

C,c=Fore.CYAN,Back.CYAN

B,b=Fore.BLACK,Back.BLACK

S=Style.BRIGHT

class Clash:

    def __init__(self,config:dict,mode="fastest"):
        self.config=config
        self.mode=mode
        self._pass=False
        self.end=False
        self.time=config["time"]
        self.statement=None
        self.inputDescription=None
        self.outputDescription=None
        self.title=None
        self.constraints=None
        self.solution=None
        self.testCases=None
        self.Clashrun_dir=os.path.join(os.environ.get("APPDATA"),"Clashrun")
        self.Clash_file=os.path.join(self.Clashrun_dir,"Clash.json")
        
    def parser(self,statement:str):
        p1=r"\[\[(.+?)\]\]"
        p2=r"\{\{(.+?)\}\}"
        p3=r"\<\<(.+?)\>\>"
        parse=re.sub(p3,fr"{Y+S}\1{W}",re.sub(p2,fr"{C}\1{W}",re.sub(p1,fr"{y}\1{b}",statement)))
        return parse
    
    def fetch_clashes(self):
        os.makedirs(self.Clashrun_dir,exist_ok=True)
        print(f"{C+S}fetching clashes...")
        time.sleep(2.7)
        print(f"{C+S}[{G}+{C+S}] payload sending...")
        clash=requests.get(self.config["site"])
        clash.raise_for_status()
        time.sleep(2.5)
        print(f"{C+S}[{G}+{C+S}] get accepted contribution clash")
        
        #separate handle in reverse,fastest,shortest handle
        fastest_handles=[]
        reverse_handles=[]
        shortest_handles=[]
        is_fastest,is_reverse,is_shortest=False,False,False
        for j,_ in enumerate(clash.json()):
            is_reverse,is_fastest,is_shortest=_.get("lastVersion").get("data").get("reverse"), _.get("lastVersion").get("data").get("fastest"), _.get("lastVersion").get("data").get("shortest")
            if is_reverse:reverse_handles.append(j)
            if is_fastest:fastest_handles.append(j)
            if is_shortest:shortest_handles.append(j)
        with open(os.path.join(self.Clashrun_dir,"reverse_handles.json"),"w") as k:
            k.write(json.dumps(reverse_handles))
        with open(os.path.join(self.Clashrun_dir,"shortest_handles.json"),"w") as k:
            k.write(json.dumps(shortest_handles))
        with open(os.path.join(self.Clashrun_dir,"fastest_handles.json"),"w") as k:
            k.write(json.dumps(fastest_handles))
        with open(self.Clash_file,"w",encoding="utf-8") as file:
            file.write(clash.text)
        time.sleep(2.3)
        print(f"{C+S}[{G}+{C+S}] fetch succesfull")
        time.sleep(1)

    
    def fetch_clash(self):
        if self.mode=="reverse":
            with open(os.path.join(self.Clashrun_dir,"reverse_handles.json"),"r") as k:
                h=json.load(k)
        elif self.mode=="fastest":
            with open(os.path.join(self.Clashrun_dir,"fastest_handles.json"),"r") as k:
                h=json.load(k)
        else:
            with open(os.path.join(self.Clashrun_dir,"shortest_handles.json"),"r") as k:
                h=json.load(k)
        with open(os.path.join(self.Clash_file),"r",encoding="utf-8") as k:
                clashes=json.load(k)
        clash=clashes[random.randint(0,len(h)-1)]
        data=clash.get("lastVersion").get("data")
        self.title=data.get("title")
        self.statement=self.parser(data.get("statement"))
        self.solution=data.get("solution")
        self.constraints=self.parser(data.get("constraints")if data.get("constraints")else "")
        self.inputDescription=self.parser(data.get("inputDescription"))
        self.outputDescription=self.parser(data.get("outputDescription"))
        self.testCases=data.get("testCases")

    def init_timer(self):
        while self.time:
            time.sleep(1.5)
            self.time-=1
        if not self.end and not self._pass:
            print()
            self.check()
    
    def check(self)->bool:
        answers=[]
        for test in self.testCases:
            with open("in.txt","w",encoding="utf-8") as f:
                f.write(test.get("testIn"))
            os.system(f"python user.py < in.txt > out.txt 2>err.txt")
            with open("out.txt","r") as f:
                out=f.read()
            with open("err.txt","r") as f:
                err=f.read()
            if out.rstrip()==test.get("testOut").rstrip():
                print(f"{Y+S}standart ouput:")
                print(out.rstrip())
                print(f"success  [{G}X{W}]")
                time.sleep(0.4)
            else:
                if err:print(f"{R+S}{err}")
                else:
                    print(f"{Y+S}standart ouput:")
                    print(out.rstrip())
                    print(f"{Y+S}Expected:")
                    print(test.get("testOut"))
                    print(f"unsuccess  [{R}X{W}]")    
                return False
        return True
    
    def clash_description(self):
        if (self.mode=="fastest" or self.mode=="shortest"):
            print()
            print(f"{W+S}mode: {C}{self.mode}\n")
            print(f"{W+S}title: {C}{self.title}\n")
            print(f"{W+S}statement:\n{W}{self.statement}\n")
            print(f"{W+S}input description:\n{W}{self.inputDescription}\n"if self.inputDescription else "")
            print(f"{W+S}output description:\n{W}{self.outputDescription}\n"if self.outputDescription else "")
            print(f"{R+S}contraintes: {W}{self.constraints}\n")
            print(f"{G}exemple.test:")
            print(f"{Y+S}input:{W}\n{self.testCases[0].get("testIn")}")
            print(f"{Y+S}output:{W}\n{self.testCases[0].get("testOut")}")
        else:
            print()
            print(f"{W+S}mode: {C}{self.mode}\n")
            print("The game mode is REVERSE: You don't have access to the statement. You need to figure out what to do by looking at the following test sets:\n")
            for i in range(min(len(self.testCases),8)):
                print(f"{G}test{i+1}:")
                print(f"{Y+S}input:{W}\n{self.testCases[i].get("testIn")}")
                print(f"{Y+S}output:{W}\n{self.testCases[i].get("testOut")}")

    def begin(self):
        self.start=True
        self.fetch_clash()
        self.clash_description()
        t=threading.Thread(target=self.init_timer)
        t.start()
        while True:
            game=input(f"{Y}clash>{W}")
            if self.time:
                if re.search(r"^(run|r)\s*$",game,re.IGNORECASE):
                    result=self.check()
                    if result:
                        self.time=1
                        self.end=True
                        break
                elif re.search(r"^(time|t)\s*$",game,re.IGNORECASE):
                    print(self.time)
                elif re.search(r"^(pass|p)\s*$",game,re.IGNORECASE):
                    self.time=1
                    self._pass=True
                    break
                elif re.search(r"^(open|o)\s*$",game,re.IGNORECASE):
                    os.system("code user.py")
            else:
                print("time out")
                break
        t.join() # wait for thread to finish,mdr
       

        
       

       
        


    