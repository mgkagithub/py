import os
from time import sleep
import random
os.system('cls')
a_list = [chr(random.randint(97, 122)) for _ in range(156*35)]
a = "".join(a_list)
l,c,l3,symbol,l1 = [],'',[],'.',[*a]
print(a)
while 1:
    for _ in range(100):
        b = random.randint(0,len(l1)-1)
        l.append(b)
    if c.isupper() == False:
        sleep(0.5)
        for i in l:
            l1[i] = l1[i].upper()
        c = ''.join(l1)
        os.system('cls')
        print(c)
        sleep(0.1)
    else:
        break