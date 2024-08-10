import sys,os
import json
import re
try:
    import requests,colorama
except ModuleNotFoundError:
    os.system("pip install requests  colorama")

from colorama import Fore,Back,init,Style
B=Fore.BLUE

R=Fore.RED

Y,y=Fore.YELLOW,Back.YELLOW

G=Fore.GREEN

W,w=Fore.WHITE,Back.WHITE

b=Back.BLACK

C=Fore.CYAN

S=Style.BRIGHT

"""
https://www.codingame.com/services/Contribution/getAcceptedContributions
{
    "id": 101820,
    "activeVersion": 5,
    "score": 2,
    "votableId": 34598400,
    "codingamerId": 6206333,
    "views": 48,
    "commentableId": 34446541,
    "title": "Transposing data",
    "status": "ACCEPTED",
    "type": "CLASHOFCODE",
    "nickname": "PackSciences",
    "publicHandle": "101820b76b348c4c0a17c3c5eeb697c498480c",
    "codingamerHandle": "c448fe147c5dc418c85052ea23e478ba3336026",
    "commentCount": 8,
    "upVotes": 2,
    "downVotes": 0
}
"""


class Clash:

    def __init__(self,mode:str,config:dict):
        self.config=config
        self.mode=mode
        self.start=False
        self.time=config["time"]
        self.statement=None
        self.input_description=None
        self.output_description=None
        self.title=None
        self.constraints=None
        self.solution=None
        self.testCases=None

    def parser(self,statement:str)->str:
        p1=r"\[\[(.+?)\]\]"
        p2=r"\{\{(.+?)\}\}"
        parse=re.sub(p2,fr"{G}\1{W}",re.sub(p1,fr"{y}\1{b}",statement))
        return parse
    
    def fetch_clash(self,handle:str):
       
        payload=[handle,True]
        response=requests.post(self.config["findcontribution"],json=payload,cookies=self.config["cookies"])
        response.raise_for_status()
        data=response.json().get("lastVersion").get("data")
        self.title=data.get("title")
        self.statement=self.parser(data.get("statement"))if self.mode!="reverse" else "This mode there is no statement,you're be given \n somes inputs,output,and just solve the problem"
        self.solution=data.get("solution")
        self.constraints=self.parser(data.get("constraints"))
        self.testCases=data.get("testCases")


       

    def begin(self):
        self.fetch_clash("101820b76b348c4c0a17c3c5eeb697c498480c")
        print()
        print(f"{W+S}mode: {C+S}{self.mode}\n")
        print(f"{W+S}title: {C+S}{self.title}\n")
        print(f"{W+S}statement:\n{W}{self.statement}\n")
        print(f"{R+S}contraintes: {W}{self.constraints}\n")
        print(f"{G}exemple.test:\n")
        print(f"input:\n{self.testCases[0].get("testIn")}")
        print(f"output:\n{self.testCases[0].get("testOut")}")
        #fetch randomly a clash in rverse:the clash handle
        #use codingame api /services/contribution/findcontribution to get the clash

        


    