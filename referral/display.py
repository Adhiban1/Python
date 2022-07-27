import json
import colorama
from colorama import Fore
colorama.init(autoreset=True)

with open('data.json', 'r') as f:
    content = json.loads(f.read())
print(type(content))
for i, j in content.items():
    userName = i
    Upline = j['Upline']
    downline = j['downline']
    wallet = j['wallet']
    string = f'''{Fore.GREEN}UserName {Fore.RED}: {Fore.MAGENTA}{userName}
{Fore.GREEN}Upline {Fore.RED}: {Fore.MAGENTA}{Upline}
{Fore.GREEN}downline {Fore.RED}: {Fore.MAGENTA}{downline}
{Fore.GREEN}wallet {Fore.RED}: {Fore.MAGENTA}{wallet}
{Fore.WHITE}------------------'''
    print(string)
input()