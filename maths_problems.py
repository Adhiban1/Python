import random
from time import sleep
from colorama import Fore
import colorama
from scipy import rand
colorama.init(autoreset=True)
import pyttsx3
import pyautogui
import threading


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
number = int(input(f'Enter the no.of Problems: '))
print(f'''{Fore.GREEN}
1.Arithmetic
2.Profit Loss
''')
choose = int(input("Choose: "))

def timer1():
    sleep(30*number)
    pyautogui.typewrite('A')
    sleep(0.1)
    pyautogui.typewrite(['enter'])

t1 = threading.Thread(target=timer1)

print()

op_list = ['+', '-', '*','/']
t_correct = 0
t_wrong = 0

def arithmetic():
    global t_correct
    global t_wrong
    for i in range(number):
        if op_list[i%4] == '/': # Division
            a = random.randint(100,1001)
            b = random.randint(3,10)
        elif op_list[i%4] == '*':
            a = random.randint(100,1001)
            b = random.randint(3,10)
        else:
            a = random.randint(10,100)
            b = random.randint(10,100)
        c = f'{a} {op_list[i%4]} {b}'
        answer = eval(c)
        print(f'{Fore.CYAN}\n{c} = {Fore.RESET}' ,end='')
        if op_list[i%4] == '/':
            qu = float(input("\nquotient: "))
            re = float(input("remainder: "))
            var = 0
        else:
            val = float(input())
            qu, re = 0, 0
        if (qu, re) == (a//b,a%b):
            print(f'{Fore.GREEN}Correct')
            engine.say('Correct')
            engine.runAndWait()
            t_correct += 1
        if val == answer:
            print(f'{Fore.GREEN}Correct')
            engine.say('Correct')
            engine.runAndWait()
            t_correct += 1
        else:
            if op_list[i%4] == '/':
                if (qu, re) != (a//b,a%b):
                    print(f'{Fore.RED}Wrong. {Fore.YELLOW}Quotient is {a//b}, Remainder is {a%b}')
                    engine.say('Wrong')
                    engine.runAndWait()
                    t_wrong += 1 
            else:
                print(f'{Fore.RED}wrong. {Fore.YELLOW}Answer is {answer}')
                engine.say('Wrong')
                engine.runAndWait()
                t_wrong += 1
        with open('math_mark.txt','w') as f:
            f.write(f'Correct = {t_correct}\nWrong = {t_wrong}')


def profit_loss():
    global t_correct
    global t_wrong
    for i in range(number):
        x = random.choices(list(range(100,1000,100)))[0]
        y = int(random.randint(int(x*0.2),int(x*1.8))/10)*10
        print(f'{Fore.CYAN}{i+1}. Buy:{x}, Sell:{y}')
        perc = input('Percent: ')
        if int(perc) == int(100*(y-x)/x):
            print(f'{Fore.GREEN}Correct')
            engine.say('Correct')
            engine.runAndWait()
            t_correct += 1
        else:
            print(f'{Fore.RED}Wrong. {Fore.YELLOW}Answer is {100*(y-x)/x} %')
            engine.say('Wrong')
            engine.runAndWait()
            t_wrong += 1
        with open('math_mark.txt','w') as f:
            f.write(f'Correct = {t_correct}\nWrong = {t_wrong}')

t1.start()

if choose == 1:
    arithmetic()
elif choose == 2:
    profit_loss()
else:
    print(f'{Fore.RED}Out of range')
print(f'{Fore.LIGHTMAGENTA_EX}\nBye bye')
sleep(5)
