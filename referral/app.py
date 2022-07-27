import json
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)
os.system("cls")

class User:
    def __init__(self, name):
        self.name = name
        self.upline = "NO"
        self.downline = []
        self.wallet = 0
    
    def addp(self, member):
        self.downline.append(member.name)
        member.upline = self.name
        self.wallet += 100

dataBase = []
with open('data.json', 'r') as f:
    dataDict = json.loads(f.read())

# dataBase.append(User("Adhiban"))
for i, (j, k) in enumerate(dataDict.items()):
    dataBase.append(User(j))
    dataBase[i].upline = k['Upline']
    dataBase[i].wallet = k['wallet']
    dataBase[i].downline = k['downline']

while True:
    print(f'{Fore.MAGENTA}\nEnter Your Name: ', end='')
    UserName = input()
    dataBase.append(User(UserName))

    for i, j in enumerate(dataBase):
        if i < len(dataBase) - 1:
            print(f'{Fore.YELLOW}{i+1}. {j.name}')
    uplineTrue = True
    while uplineTrue:
        print(f'{Fore.CYAN}Enter the upline name: ',end='')
        Upline = input()
        for i in dataBase:
            if Upline == i.name:
                i.addp(dataBase[-1])
                uplineTrue = False
                print(f'{Fore.GREEN}[ACCOUNT CREATED]')
                break
        else:
            print(f"{Fore.RED}Wrong upline Name...Enter again...\n")
    savedata = {}
    for i in dataBase:
        savedata[i.name] = {'Upline' : i.upline, 'downline' : i.downline, 'wallet' : i.wallet}
    with open("data.json", "w") as f:
        f.write(json.dumps(savedata))