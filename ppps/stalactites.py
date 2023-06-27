import os
from time import sleep
import random
os.system('cls')
a,l,c,l3 = "idsbdkfhsblidfgbgsigvubgiaurbvlavbiusdhvushlvuhsdkyvgskyfgvalsudufgftjfcmtgderswhrsrtfyoghvmhvmgsjtkdgdfjhefhjfsjhfkjhfjhfbjfvbxjfhljhfkhfbfhhglihflhdjhvbfj",[],'',[]
# len of a = 156 for the best effect , also ctrl+b
l1 = [*a]
symbol = ' '
# while 1:
#     for _ in range(5):
#         b = random.randint(0,len(l1)-1)
#         l.append(b)
#     if c.isupper() == False:
#         sleep(0.5)
#         for i in l:
#             l1[i] = l1[i].upper()
#         c = ''.join(l1)
#         print(c)
#     else:
#         break
print(a)
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
