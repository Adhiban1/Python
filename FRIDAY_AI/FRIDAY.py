### Ironman's FRIDAY AI
# Import Files
from colorama import Fore
from playsound import playsound
import codecs
import pyttsx3
import keyboard
import os
from gtts import gTTS
from time import sleep, ctime
from getpass import getpass
import colorama
colorama.init(autoreset=True)

all_functions = '''
Functions: Exam, Shutdown, Add Data, Chances'''

# Functions


def chances():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    chance = int(input(f'{Fore.YELLOW}Enter the Chances: '))
    for i in range(chance*2+1):
        while True:
            if keyboard.is_pressed('space'):
                sleep(1)
                if i % 2 == 0:
                    if chance - i/2 - 1 != 0 and chance - i/2 - 1 != -1:
                        print(
                            f'Now You have only {int(chance - i/2 -1)} chance')
                        engine.say(
                            f'Now You have only {int(chance - i/2 -1)} chance')
                        engine.runAndWait()
                    elif chance - i/2 - 1 == -1:
                        print('Good Bye')
                        engine.say('Good Bye')
                        engine.runAndWait()
                        os.system('taskkill /im chrome.exe')
                    else:
                        print('This is Last')
                        engine.say('This is last')
                        engine.runAndWait()
                print(i)
                break


def exam():
    os.system('cls')
    colour = [
        Fore.RED,
        Fore.BLUE,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.CYAN,
        Fore.MAGENTA
    ]
    for i in range(126000):
        h = ctime()[11:13]
        m = ctime()[14:16]
        s = ctime()[17:19]
        (h, m, s) = tuple(map(int, (h, m, s)))
        print(f'{Fore.RED}{h}{Fore.RESET}:{Fore.GREEN}{m}{Fore.RESET}:{Fore.CYAN}{s}')
        if s <= 30 and m % 30 == 0:
            print(
                f'{colour[i%6]}Timeout, {colour[(i+1)%6]}Start {colour[(i+2)%6]}Next Question')
        sleep(0.1)
        os.system('cls')


def shut_down():
    os.system('shutdown /s')


def c_time():
    s = ctime().split()
    return f'{s[0]}-{s[1]}-{s[2]}-{s[4]} {s[3]}'


def add_data():
    if_this = input(f'{Fore.GREEN}if this: ')
    then_that = input(f'{Fore.GREEN}then that: ')
    add_string = '\n' + if_this + ' > ' + then_that
    with open('FRIDAY.txt', 'a') as f:
        f.write(add_string)


def alarm():
    pass
####################################################


a = 'en'
# Main Function


def FRIDAY():
    os.system('cls')
    print(f"{Fore.LIGHTRED_EX}Artifitial Intellegent FRIDAY created by V.Adhiban Siddarth\n")
    # sleep(2)

    def speak(text):
        try:
            k = gTTS(text=text, lang=a)
            file = 'speech_r.mp3'
            k.save(file)
            sleep(0.5)
            playsound(file)
        except:
            print(
                f'{Fore.RED}Some audio error... it is not your fault... Try again...Press Enter')

    with codecs.open('FRIDAY.txt', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    print(f'{Fore.YELLOW}{content}')
    print(f'{Fore.CYAN}{all_functions}')
    print(Fore.BLUE + '_'*100)
    print(f"\n{Fore.RED}({Fore.MAGENTA}{c_time()}{Fore.RED}){Fore.GREEN} 'FRIDAY' {Fore.RED}$ ", end='')
    speak('Hello I am Friday How can I help you!')
    line_list = content.split('\n')
    seperate_list = []
    for i in line_list:
        k = i.split(' > ')
        seperate_list.append([k[0], k[1]])

    # Main loop
    while True:
        text = input()
        if 'quit' in text.lower():
            break
        elif 'shutdown' in text.lower():
            shut_down()
        elif 'add data' in text.lower():
            add_data()
        elif 'alarm' in text.lower():
            alarm()
        elif 'exam' in text.lower():
            exam()
        elif 'chances' in text.lower():
            chances()
        else:
            for i in seperate_list:
                if i[0].lower() in text.lower():
                    print(f'{Fore.CYAN}{i[1]}')
                    speak(i[1])
                    break
        print(
            f"\n{Fore.RED}({Fore.MAGENTA}{c_time()}{Fore.RED}){Fore.GREEN} 'FRIDAY' {Fore.RED}$ ", end='')
    ##############


# Password
for i in range(3):
    pass1 = getpass('Password: ')
    os.system('cls')
    if pass1 == '1357':
        print(f'{Fore.GREEN}Correct Password...\n')
        sleep(1)
        FRIDAY()
        break
    elif i < 2:
        print(f'{Fore.RED}Enter again... You have {2-i} chance.\n')
    else:
        print(f'{Fore.YELLOW}You chance over Bye...')
