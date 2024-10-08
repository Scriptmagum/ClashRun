import readline
import sys,os
import json
import re
import time
import random
import threading  # i love that ,fork process lol
from config import *
import subprocess
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests



class Clash:

    def __init__(self,mode="fastest"):
        self.mode=mode
        self._pass=False
        self.end=False
        self.time=int(config["clash_time"])*60
        self.statement=None
        self.inputDescription=None
        self.outputDescription=None
        self.title=None
        self.constraints=None
        self.solution=None
        self.solution_lang=None
        self.sol_file=config["langage"]
        self.testCases=None
        self.Clashrun_dir=os.path.join(os.path.expanduser("~"),".Clashrun")
        self.Clash_file=os.path.join(self.Clashrun_dir,"Clash.json")
        
    def parser(self,statement:str):
        p1=r"\[\[(.+?)\]\]"
        p2=r"\{\{(.+?)\}\}"
        p3=r"\<\<(.+?)\>\>"
        parse=re.sub(p3,fr"{Y+S}\1{reset}{W}",re.sub(p2,fr"{C}\1{reset}{W}",re.sub(p1,fr"{y}\1{reset}{W}",statement)))
        return parse
    
    def fetch_clashes(self):
        os.makedirs(self.Clashrun_dir,exist_ok=True)
        print(f"{C+S}fetching clashes...{reset+W}")
        time.sleep(2.7)
        print(f"{C+S}[{G}+{C+S}] payload sending...{reset+W}")
        clash=requests.get(config["site"])
        clash.raise_for_status()
        time.sleep(2.5)
        print(f"{C+S}[{G}+{C+S}] get accepted contribution clash{reset+W}")
        
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
        print(f"{C+S}[{G}+{C+S}] fetch succesfull{reset+W}")
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
        with open(self.Clash_file,"r",encoding="utf-8") as k:
                clashes=json.load(k)
        clash=clashes[h[random.randint(0,len(h)-1)]]
        data=clash.get("lastVersion").get("data")
        self.title=data.get("title")
        self.statement=self.parser(data.get("statement"))
        self.solution=data.get("solution")
        self.constraints=self.parser(data.get("constraints")if data.get("constraints")else "")
        self.inputDescription=self.parser(data.get("inputDescription"))
        self.outputDescription=self.parser(data.get("outputDescription"))
        self.solution_lang=data.get("solutionLanguage")
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
        if self.mode=="shortest":
            with open(f"Assets/user.{self.sol_file}","r") as f:
                content=f.read().strip('\n')
            if len(content)>int(config['limit_characters']):
                print(f"{R}characters limit exceed. must be <<{config['limit_characters']}{reset+W}")
                return False
        for test in self.testCases:
            with open("Assets/in.txt","w",encoding="utf-8") as f:
                f.write(test.get("testIn"))
        
            command=[langs[self.sol_file],f"Assets/user.{self.sol_file}"]
            try:
                result=subprocess.run(command,stdin=open("Assets/in.txt","r"),stdout=open("Assets/out.txt","w"),stderr=open("Assets/err.txt","w"),timeout=10)
            except subprocess.TimeoutExpired:
                print(f"{R}time limit exceed.please try again{reset+W}")
                return False
            except:
                raise  Exception(f"{R}{langs[self.sol_file]} not found.try ./install.sh to install all dependencies")
                quit()

            #os.system(f"python user.py < in.txt > out.txt 2>err.txt")
            with open("Assets/out.txt","r") as f:
                out=f.read()
            with open("Assets/err.txt","r") as f:
                err=f.read()
            if out.rstrip()==test.get("testOut").rstrip():
                print(f"{Y+S}standart output:{reset+W}")
                print(f"{W}{out.rstrip()}{reset+W}")
                print(f"{g}success{reset}{W}  [{G}X{W}]{reset+W}")
                time.sleep(0.4)
            else:
                if err:print(f"{R+S}{err}{reset+W}")
                else:
                    print(f"{Y+S}standart output:{reset+W}")
                    print(f"{W}{out.rstrip()}{reset+W}")
                    print(f"{Y+S}Expected:{reset+W}")
                    print(f"{W}{test.get('testOut')}{reset+W}")
                    print(f"{r}unsuccess{reset}{W}  [{R}X{W}]{reset+W}")    
                return False
        return True
    def show_testcases(self):
        i=1
        for test in self.testCases:
                if test.get("isTest"):
                    print(f"{G}test{i}:{reset+W}")
                    print(f"{Y+S}input:{reset+W}\n{test.get('testIn').rstrip()}{reset+W}")
                    print(f"{Y+S}output:{reset+W}\n{test.get('testOut').rstrip()}{reset+W}")
                    i+=1
    
    def clash_description(self):
        if (self.mode=="fastest" or self.mode=="shortest"):
            print()
            print(f"{W+S}mode: {reset+C}{self.mode}{reset+W}\n")
            print(f"{W+S}title: {reset+C}{self.title}{reset+W}\n")
            print(f"{W+S}statement:\n{reset+W}{self.statement}{reset+W}\n")
            print(f"{W+S}input description:\n{reset+W}{self.inputDescription}{reset+W}\n"if self.inputDescription else "{reset+W}")
            print(f"{W+S}output description:\n{reset+W}{self.outputDescription}{reset+W}\n"if self.outputDescription else f"{reset+W}")
            print(f"{R+S}contraintes: {reset+W}{self.constraints}{reset+W}\n")
            print(f"{G}exemple.test:{reset+W}")
            print(f"{Y+S}input:{reset+W}\n{self.testCases[0].get('testIn')}{reset+W}")
            print(f"{Y+S}output:{reset+W}\n{self.testCases[0].get('testOut')}{reset+W}")
        else:
            print()
            print(f"{W+S}mode: {C}{self.mode}{reset+W}\n")
            print(f"{W}The game mode is REVERSE: You don't have access to the statement. You need to figure out what to do by looking at the following test sets:{reset+W}\n")
            self.show_testcases()
    def show_char(self):
        if self.mode=="shortest":
            with open(f"Assets/user.{self.sol_file}","r") as f:
                content=f.read().strip('\n')
            print(f"{W}{len(content)}{reset+W}")
    def begin(self):
        self.start=True
        self.fetch_clash()
        self.clash_description()
        t=threading.Thread(target=self.init_timer)
        t.start()
        while True:
            game=input(f"{Y}<clash\\>{reset}{W}")
            search=re.search(r"^\s*(open|o)\s+(py|rb|sh|pl|js)\s*$|^open\s*$",game,re.IGNORECASE)
            if self.time:
                if re.search(r"^\s*(run|r)\s*$",game,re.IGNORECASE):
                    result=self.check()
                    if result:
                        self.time=1
                        self.end=True
                        break
                elif re.search(r"^\s*(time|t)\s*$",game,re.IGNORECASE):
                    tim=self.time
                    print(f"{tim//60}:{tim%60}")
                elif re.search(r"^\s*(pass|p)\s*$",game,re.IGNORECASE):
                    self.time=1
                    self._pass=True
                    break
                elif search:
                    self.sol_file=search.group(2).lower() if search.group(2) else config["langage"]
                   
                    os.system(f"{config['editor']}  Assets/user.{self.sol_file}")
                   
                elif re.search(r"^\s*(tests|testcases)\s*$",game,re.IGNORECASE):
                    self.show_testcases()

                elif re.search(r"^\s*(help|h)\s*$",game,re.IGNORECASE):
                    print(help_clash)
                elif re.search(r"^\s*(char|c)\s*$",game,re.IGNORECASE):
                    self.show_char()
                else:
                    print(f"\n{W}try to see: {Y+S}help {W}please{reset+W}\n")
            else:
                print(f"{R+S}time out{reset+W}")
                break
        t.join() # wait for thread to finish,mdr
       

        
       

       
        


    
