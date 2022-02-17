import requests
import bs4
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

str3 = '''1. How does a transmission gate produce fully restored logic output? 
2. Define low noise margin and high noise margin of a CMOS inverter. 
3. State the operations performed during pre charge and evaluate phase of 
dynamic circuits. 
4. List the sources of power dissipation in CMOS circuits. 
5. What is meant by bistability? 
6. Define clock skew in digital circuits. 
7. Draw the circuit diagram of 1-bit binary shifter using MOS transistor. 
8. State the need of a sense amplifier in a memory cell. 
9. List the common techniques for ad hoc testing. 
10. What are the limitations of IDDQ testing?
'''
#
str3 = str3.replace('.\n','\n')
list1 = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ']
for j in list1:
    str3 = str3.replace(j,'')
str3 = str3.replace(' ','+')
list2 = str3.split('\n')
#list2.pop()
#

f = open('web_scrap.txt', 'w')

for i in list2:
    try:
        url = "https://www.google.com/search?q=" + i
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        content = soup.find( "div" , class_='BNeawe' ).text 
        print('\n' + f'{Back.MAGENTA}' +  i.replace('+',' ') + ':')
        f.write( i.replace('+',' ') + ':'+ '\n')
        print(f'{Fore.CYAN}' +content)
        f.write(content + '\n\n')
    except:
        print("Error")
print(f'{Fore.YELLOW}\nFinish..............................')
f = open('web_scrap.txt', 'r')
while True:
    pass
