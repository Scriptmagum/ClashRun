import os,sys,json,time
from colorama import Fore,Back,Style,init
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
with open("config.json","r") as file:
    config=json.load(file)
init(autoreset=True)
B=Fore.BLUE

R=Fore.RED

Y=Fore.YELLOW

G=Fore.GREEN

W=Fore.WHITE

C=Fore.CYAN

S=Style.BRIGHT
Clashrun_dir=os.path.join(os.environ.get("APPDATA"),"Clashrun")
os.makedirs(Clashrun_dir,exist_ok=True)

#fetch all data from codingame api
def fetch():
    clashes=[]
    print(f"{C+S}fetching clashes...")
    time.sleep(5)
    payload=["CLASHOFCODE"]
    print(f"{C+S}[{G}+{C+S}] payload sending...")
    response=requests.post(config["acceptedcontribution"],json=payload,cookies=config["cookies"])
    response.raise_for_status()
    handles=[_.get("publicHandle") for _ in response.json()]
    for handle in handles:
        payload=[handle,'True']
        response=requests.post(config["findcontribution"],json=payload,cookies=config["cookies"])
        clashes+=[response.text]
    time.sleep(2.5)
    print(f"{C+S}[{G}+{C+S}] get accepted contribution clash")
    with open(os.path.join(Clashrun_dir,"Clash.json"),"w",encoding="utf-8") as file:
        try:
            file.write('['+','.join(clashes)+']')
            time.sleep(2.3)
            print(f"{C+S}[{G}+{C+S}] fetch succesfull")

        except FileNotFoundError:
            print("File or directory not found")
            
if __name__=="__main__":
    fetch()