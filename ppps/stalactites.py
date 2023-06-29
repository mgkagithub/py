import os
from time import sleep
import random
os.system('cls')
a_list = [chr(random.randint(97, 122)) for _ in range(156)]
a = "".join(a_list)
l,c,l3,symbol,l1 = [],'',[],input("Enter the symbol you want to replace with alphabets: \n-> "),[*a]
stalact_wtd = input("Do u want to see the animation or stalactites: \n1> stalactites - s\n2> animation - a\n-> ")
print(a)
if stalact_wtd.lower() == 'a':
    while l1.count(symbol)!=len(l1):
        for _ in range(5):
            b = random.randint(0,len(l1)-1)
            if b not in l:
                l.append(b)
        if c.isalpha()==False:
            for i in l:
                if l1[i]==symbol:
                    pass
                else:
                    l1[i] = symbol
            c = ''.join(l1)
            os.system('cls')
            print(c)
            sleep(0.1)
        else:
            break
elif stalact_wtd.lower() == 's':
    while l1.count(symbol)!=len(l1):
        for _ in range(5):
            b = random.randint(0,len(l1)-1)
            if b not in l:
                l.append(b)
        if c.isalpha()==False:
            for i in l:
                if l1[i]==symbol:
                    pass
                else:
                    l1[i] = symbol
            c = ''.join(l1)
            print(c)
        else:
            break 
else:
    print('Invalid input.')