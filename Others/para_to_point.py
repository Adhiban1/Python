#!/usr/bin/env python
# coding: utf-8

# In[35]:


from colorama import Fore
import colorama
colorama.init(autoreset=True)
#from random import choices

color_l = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.MAGENTA,
    Fore.RED,
    Fore.WHITE,
    Fore.YELLOW
]
with open('Hello.txt', 'r') as f:
    content = f.read()
str1 = content
list1 = str1.split()
str2 = '1. '
num = 1
for i in list1:
    str2 += i + ' '
    if ('.' in i) or ('?' in i) or (':' in i):
        num += 1
        str2 += f'\n{num}. '
list2 = str2.split(' \n')
list2.pop()
m = 0
for i in list2:
    print(color_l[m%7] + i)
    m += 1

while True:
    pass
