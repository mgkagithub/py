import os
from time import sleep
import random
os.system('cls')
a_list = [chr(random.randint(97, 122)) for _ in range(156)]
a = "".join(a_list)
l,c,l3,symbol,l1 = [],'',[],'.',[*a]
capital_wtd = input("Do u want to see the animation as linear or random: \n1> linear - l\n2> random - r\n-> ")
if capital_wtd.lower() == 'r':
    print(a)
    while 1:
        for _ in range(350):
            b = random.randint(0,len(l1)-1)
            l.append(b)
        if c.isupper() == False:
            for i in l:
                l1[i] = l1[i].upper()
            c = ''.join(l1)
            os.system('cls')
            print(c)
            sleep(0.05)
        else:
            break
elif capital_wtd.lower() == 'l':
    print(a)
    i = 0
    while 1:
        l1[i] = l1[i].upper()
        c = ''.join(l1)
        os.system('cls')
        print(c)
        i += 1