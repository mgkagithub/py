import os
from time import sleep
import random
import string
os.system('cls')
a_list = list(chr(random.randint(97, 122)) for _ in range(156*35))
a = ''.join(a_list)
print(a)
name = input("Enter your string: (25 words)\n-> ")
l,c,l3,symbol,l1,name_letter_index,i,j,str1,str2,start_index = [],'',[],'.',[*a],[],0,0,name,a,0
name_list = [char for char in ''.join(name.split()) if char.isalpha() and char not in string.punctuation and char not in string.digits]
name_list = [elem.lower() for elem in name_list]
for char in name_list:
    index = str2.find(char, start_index)
    if index != -1:
        name_letter_index.append(index)
        start_index = index + 1
print(a)
while l1.count(symbol) != len(l1):
    for _ in range(100):
        b = random.randint(0, len(l1) - 1)
        if b not in l and b not in name_letter_index:
            l.append(b)
    if c.isalpha() == False:
        for i in l:
            if l1[i] == symbol:
                pass
            else:
                l1[i] = symbol
        c = ''.join(l1)
        os.system('cls')
        print(c)
        sleep(0.1)
        if (len(l1)-l1.count(symbol))==len(name_list):
            os.system('cls')
            break
    else:
        break
print('\n'+name+'\n')
print(c)
   
