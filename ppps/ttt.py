
import random
from time import sleep
import datetime
import os 
import math

def ttt():

    print("Let's play Tic-Tac-Toe!!!")

    tl=' '
    tm=' '
    tr=' '
    ml=' '
    mm=' '
    mr=' '
    bl=' '
    bm=' '
    br=' '

    l=[[tl,tm,tr],[ml,mm,mr],[bl,bm,br]]
    l1=[['tl','tm','tr'],['ml','mm','mr'],['bl','bm','br']]
    l2=['tl','tm','tr','ml','mm','mr','bl','bm','br']

    d=['Easy','Medium','Hard']

    def check_1():
        for i in range(3):
            if l[i][0]==l[i][1] and l[i][0]==l[i][2] and l[i][0]!=' ':
                return l[i][0]
            elif l[0][i]==l[1][i] and l[0][i]==l[2][i] and l[0][i]!=' ':  
                return l[0][i]
            elif l[0][0]==l[1][1] and l[0][0]==l[2][2] and l[0][0]!=' ':
                return l[0][0]
            elif l[0][2]==l[1][1] and l[0][2]==l[2][0] and l[0][2]!=' ':
                return l[0][2]
        else:
            return ''

    def check_2():
        if l[0][0]==l[1][1] and l[2][2]==' ' and l[0][0]==p:
            return l1[2][2]
        elif l[0][0]==l[2][2] and l[1][1]==' ' and l[0][0]==p:
            return l1[1][1]
        elif l[1][1]==l[2][2] and l[0][0]==' ' and l[1][1]==p:
            return l1[0][0]
        elif l[0][2]==l[1][1] and l[2][0]==' ' and l[0][2]==p:
            return l1[2][0]
        elif l[0][2]==l[2][0] and l[1][1]==' ' and l[0][2]==p:
            return l1[1][1]
        elif l[2][0]==l[1][1] and l[0][2]==' ' and l[2][0]==p:
            return l1[0][2]
        else:
            for i in range(3):
                if l[i][0]==l[i][1] and l[i][2]==' ' and l[i][0]==p:
                    return l1[i][2]
                elif l[i][0]==l[i][2] and l[i][1]==' ' and l[i][0]==p:
                    return l1[i][1]
                elif l[i][1]==l[i][2] and l[i][0]==' ' and l[i][1]==p:
                    return l1[i][0]
                elif l[0][i]==l[1][i] and l[2][i]==' ' and l[0][i]==p:
                    return l1[2][i]
                elif l[0][i]==l[2][i] and l[1][i]==' ' and l[0][i]==p:
                    return l1[1][i]
                elif l[1][i]==l[2][i] and l[0][i]==' ' and l[1][i]==p:
                    return l1[0][i]
            else:
                return ''

    def check_3():
        if l[0][0]==l[1][1] and l[2][2]==' ' and l[0][0]==c:
            return l1[2][2]
        elif l[0][0]==l[2][2] and l[1][1]==' ' and l[0][0]==c:
            return l1[1][1]
        elif l[1][1]==l[2][2] and l[0][0]==' ' and l[1][1]==c:
            return l1[0][0]
        elif l[0][2]==l[1][1] and l[2][0]==' ' and l[0][2]==c:
            return l1[2][0]
        elif l[0][2]==l[2][0] and l[1][1]==' ' and l[0][2]==c:
            return l1[1][1]
        elif l[2][0]==l[1][1] and l[0][2]==' ' and l[2][0]==c:
            return l1[0][2]
        else:
            for i in range(3):
                if l[i][0]==l[i][1] and l[i][2]==' ' and l[i][0]==c:
                    return l1[i][2]
                elif l[i][0]==l[i][2] and l[i][1]==' ' and l[i][0]==c:
                    return l1[i][1]
                elif l[i][1]==l[i][2] and l[i][0]==' ' and l[i][1]==c:
                    return l1[i][0]
                elif l[0][i]==l[1][i] and l[2][i]==' ' and l[0][i]==c:
                    return l1[2][i]
                elif l[0][i]==l[2][i] and l[1][i]==' ' and l[0][i]==c:
                    return l1[1][i]
                elif l[1][i]==l[2][i] and l[0][i]==' ' and l[1][i]==c:
                    return l1[0][i]
            else:
                return ''

    def grid():
        os.system('cls')
        #os.system('clear')#os.system('cls')
        print('\n')
        print('\t',end='')
        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
        print('\t',end='')
        print("---+-----+---")
        print('\t',end='')
        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
        print('\t',end='')
        print("---+-----+---")
        print('\t',end='')
        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
        print('\n')
        print()

    while True:
        n=input("How many player/s are playing?")
        if n=='1':
            while True:
                print("Difficulty levels:\n1.Easy\n2.Medium\n3.Hard\n4.Random")
                ch=input("Enter the difficulty level:")
                if ch not in ('1','2','3','4'):
                    print("Invalid Input!!")
                else:
                    break

            ch0=''
            if ch=='4':
                ch0='4'
                ch=random.choice(['1','2','3'])
                dd=d[int(ch)-1]

            while True:
                a=input("Choose: x or o >")
                p=a.lower()
                if p not in ('x','o'):
                    print("Invalid input")
                    continue
                else:
                    break

            if p=='x':
                c='o'
                print("You have chosen x and therefore I have o")
            elif p=='o':
                c='x'
                print("You have chosen o and therefore I have x")
            print("Name of the cells are tl for top left, tm for top middle, tr for top right, ml for middle left, mm for middle middle, mr for middle right, bl for bottom left, bm for bottom middle, br for bottom right.")
            
            print()
            print('tl',"|",'tm',"|",'tr')
            print("---+----+---")
            print('ml',"|",'mm',"|",'mr')
            print("---+----+---")
            print('bl',"|",'bm',"|",'br')
            print()
            print("For your reference(if you want)")
            print()
            
            sleep(5)

            print("Best of luck!!")
            print("Let the battle begin!!")

            if ch=='1':
                if c=='x':
                    print("I will start!")
                    z=0
                    while True:
                        z+=1
                        r=random.choice(l2)
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==r:
                                    l[i][j]='x'
                        l2.remove(r)
                        
                        grid()
                        print(f"I have put x at {r}")

                        k=check_1()
                        if k=='o':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='x':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break

                        while True:
                            x1=str(input("Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        grid()
                        
                        
                        k=check_1()
                        if k=='o':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='x':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break
            
                elif c=='o':
                    print("You will start!")
                    while True:
                        while True:
                            x1=str(input("Where do you want to put x?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='x'
                        
                        grid()
                            
                        k=check_1()
                        if k=='x':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='o':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break

                        r=random.choice(l2)
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==r:
                                    l[i][j]='o'
                        l2.remove(r)

                        grid()
                        
                        print(f"I have put o at {r}")

                        k=check_1()
                        if k=='x':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='o':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break
            
            elif ch=='2':
                if c=='x':
                    print("I will start!")
                    while True:
                        j=check_3()
                        if j=='':
                            j=check_2()
                            if j=='':
                                r=random.choice(l2)
                            else:
                                r=j
                        else:
                            r=j        
                        l2.remove(r)
                        
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==r:
                                    l[i][j]='x'

                        grid()
                        
                        print(f"I have put x at {r}")

                        k=check_1()
                        if k=='o':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='x':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break

                        while True:
                            x1=str(input("Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        grid()
                        
                        
                        k=check_1()
                        if k=='o':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='x':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break
            
                elif c=='o':
                    print("You will start!")
                    while True:
                        while True:
                            x1=str(input("Where do you want to put x?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='x'
                        
                        grid()
                        
                            
                        k=check_1()
                        if k=='x':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='o':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break

                        j=check_3()
                        if j=='':
                            j=check_2()
                            if j=='':
                                r=random.choice(l2)
                            else:
                                r=j
                        else:
                            r=j        
                        l2.remove(r)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==r:
                                    l[i][j]='o'

                        grid()
                        
                        print(f"I have put o at {r}")

                        k=check_1()
                        if k=='x':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='o':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break

            elif ch=='3':
                if c=='x':
                    print("I will start!")
                    r=random.choice(['t1','t2'])
                    if r=='t1':
                        z=[]
                        i=0
                        w=-1
                        l3=['tl','tr','bl','br']
                        while True:
                            w+=1
                            i+=1
                            j=check_3()
                            if j=='':
                                j=check_2()
                                if j=='':
                                    if i==1:
                                        while True:
                                            x=random.choice(l3)
                                            if x in z:
                                                continue
                                            else:
                                                break
                                        l3.remove(x)
                                        l2.remove(x)
                                        z.append(x)
                                        e=x
                                    
                                    elif i!=1:
                                        if 'mm' not in l2:
                                            if l3!=[]:
                                                while True:
                                                    x=random.choice(l3)
                                                    if x in z:
                                                        continue
                                                    else:
                                                        break
                                                l3.remove(x)
                                                l2.remove(x)
                                                z.append(x)
                                            else:
                                                while True:
                                                    x=random.choice(l2)
                                                    if x in z:
                                                        continue
                                                    else:
                                                        break
                                                l2.remove(x)
                                                z.append(x)

                                        else:
                                            if w==1:
                                                if x1[0]==x[0] or x1[1]==x[1]:
                                                    while True:
                                                        x=random.choice(l3)
                                                        if x1[0]==x[0] or x1[1]==x[1]:
                                                            continue
                                                        elif x[0]!=e[0] and x[1]!=e[1]:
                                                            continue
                                                        else:
                                                            break
                                                    l3.remove(x)
                                                else:
                                                    while True:
                                                        x=random.choice(l3)
                                                        if x[0]!=e[0] and x[1]!=e[1]:
                                                            continue
                                                        else:
                                                            break
                                                    l3.remove(x)
                                            else:
                                                while True:
                                                    x=random.choice(l3)
                                                    if x[0]==e[0] or x[1]==e[1]:
                                                        continue
                                                    else:
                                                        break
                                                l3.remove(x)
                                            
                                            if x in l2:
                                                l2.remove(x)
                                                if x in l3:
                                                    l3.remove(x)
                                            z.append(x)

                                else:
                                    x=j
                                    l2.remove(x)
                                    z.append(x)
                                    if x in l3:
                                        l3.remove(x)

                            else:
                                x=j
                                l2.remove(x)
                                z.append(x)
                                if x in l3:
                                    l3.remove(x)

                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]==x:
                                        l[i][j]='x'
                                        
                            grid()
                            

                            print(f"I have put x at {x}")

                            k=check_1()
                            if k=='o':
                                print("You won!!")
                                break
                            elif k=='x':
                                print("I won!!")
                                print("≧◔◡◔≦")
                                break
                            elif k=='':
                                if l2==[]:
                                    print("Draw!!")
                                    break

                            while True:
                                x1=str(input(f"Where do you want to put o?"))
                                if x1 not in l2:
                                    print("Invalid input")
                                    continue
                                else:
                                    break
                            l2.remove(x1)
                            if x1 in l3:
                                l3.remove(x1)
                            z.append(x1)

                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]==x1:
                                        l[i][j]='o'

                            grid()
                            

                            k=check_1()
                            if k=='o':
                                print("You won!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break
                            elif k=='x':
                                print("I won!!")
                                print("≧◔◡◔≦")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break
                            elif k=='':
                                if l2==[]:
                                    print("Draw!!")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break

                    elif r=='t2':
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]=='mm':
                                    l[i][j]='x'
                                    l2.remove('mm')

                        grid()
                        print("I have put x at mm")

                        while True:
                            x=str(input(f"Where do you want to put o?"))
                            if x not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x:
                                    l[i][j]='o'
                                    l2.remove(x)
                        
                        grid()
                    
                        if x in ['tm','ml','mr','bm']:
                            if x=='tm':
                                y=random.choice(['tl','tr'])
                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==y:
                                            l[i][j]='x'
                                            l2.remove(y)
                                
                                grid()
                                print(f"I have put x at {y}")

                                while True:
                                    x1=str(input(f"Where do you want to put o?"))
                                    if x1 not in l2:
                                        print("Invalid input")
                                        continue
                                    else:
                                        break
                                l2.remove(x1)

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x1:
                                            l[i][j]='o'

                                grid()

                                c2=check_3()
                                if c2=='':
                                    c1=check_2()
                                    if c1=='':
                                        if y=='tl':
                                            x='bl'
                                        elif y=='tr':
                                            x='br'
                                    else:
                                        x=c1
                                else:
                                    x=c2

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x:
                                            l[i][j]='x'
                                l2.remove(x)
                                
                                grid()
                                print(f"I have put x at {x}")

                                while True:
                                    x1=str(input(f"Where do you want to put o?"))
                                    if x1 not in l2:
                                        print("Invalid input")
                                        continue
                                    else:
                                        break

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x1:
                                            l[i][j]='o'
                                l2.remove(x1)

                                grid()

                                c=check_3()
                                if c=='':
                                    c=check_2()
                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==c:
                                            l[i][j]='x'
                                l2.remove(c)

                                grid()
                                print(f"I have put x at {c}")

                                k=check_1()
                                if k=='o':
                                    print("You won!!")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='x':
                                    print("I won!!")
                                    print("≧◔◡◔≦")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='':
                                    if l2==[]:
                                        print("Draw!!")
                                        if ch0=='4':
                                            print()
                                            print(f"Difficulty: {dd}")
                                        break

                            elif x=='ml':
                                y=random.choice(['tl','bl'])
                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==y:
                                            l[i][j]='x'
                                            l2.remove(y)
                                
                                grid()
                                print(f"I have put x at {y}")

                                while True:
                                    x1=str(input(f"Where do you want to put o?"))
                                    if x1 not in l2:
                                        print("Invalid input")
                                        continue
                                    else:
                                        break
                                l2.remove(x1)

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x1:
                                            l[i][j]='o'

                                grid()

                                c2=check_3()
                                if c2=='':
                                    c1=check_2()
                                    if c1=='':
                                        if y=='tl':
                                            x='tr'
                                        elif y=='bl':
                                            x='br'
                                    else:
                                        x=c1
                                else:
                                    x=c2

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x:
                                            l[i][j]='x'
                                l2.remove(x)
                                
                                grid()
                                print(f"I have put x at {x}")

                                while True:
                                    x1=str(input(f"Where do you want to put o?"))
                                    if x1 not in l2:
                                        print("Invalid input")
                                        continue
                                    else:
                                        break

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x1:
                                            l[i][j]='o'
                                l2.remove(x1)

                                grid()

                                c=check_3()
                                if c=='':
                                    c=check_2()
                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==c:
                                            l[i][j]='x'
                                l2.remove(c)

                                grid()
                                print(f"I have put x at {c}")
                                
                                k=check_1()
                                if k=='o':
                                    print("You won!!")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='x':
                                    print("I won!!")
                                    print("≧◔◡◔≦")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='':
                                    if l2==[]:
                                        print("Draw!!")
                                        if ch0=='4':
                                            print()
                                            print(f"Difficulty: {dd}")
                                        break

                            elif x=='mr':
                                y=random.choice(['tr','br'])
                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==y:
                                            l[i][j]='x'
                                            l2.remove(y)
                                
                                grid()
                                print(f"I have put x at {y}")

                                while True:
                                    x1=str(input(f"Where do you want to put o?"))
                                    if x1 not in l2:
                                        print("Invalid input")
                                        continue
                                    else:
                                        break
                                l2.remove(x1)

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x1:
                                            l[i][j]='o'

                                grid()

                                c2=check_3()
                                if c2=='':
                                    c1=check_2()
                                    if c1=='':
                                        if y=='tr':
                                            x='tl'
                                        elif y=='br':
                                            x='bl'
                                    else:
                                        x=c1
                                else:
                                    x=c2

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x:
                                            l[i][j]='x'
                                l2.remove(x)
                                
                                grid()
                                print(f"I have put x at {x}")

                                while True:
                                    x1=str(input(f"Where do you want to put o?"))
                                    if x1 not in l2:
                                        print("Invalid input")
                                        continue
                                    else:
                                        break

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x1:
                                            l[i][j]='o'
                                l2.remove(x1)

                                grid()

                                c=check_3()
                                if c=='':
                                    c=check_2()
                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==c:
                                            l[i][j]='x'
                                l2.remove(c)

                                grid()
                                print(f"I have put x at {c}")

                                k=check_1()
                                if k=='o':
                                    print("You won!!")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='x':
                                    print("I won!!")
                                    print("≧◔◡◔≦")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='':
                                    if l2==[]:
                                        print("Draw!!")
                                        if ch0=='4':
                                            print()
                                            print(f"Difficulty: {dd}")
                                        break

                            elif x=='bm':
                                y=random.choice(['bl','br'])
                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==y:
                                            l[i][j]='x'
                                            l2.remove(y)
                                
                                grid()
                                print(f"I have put x at {y}")

                                while True:
                                    x1=str(input(f"Where do you want to put o?"))
                                    if x1 not in l2:
                                        print("Invalid input")
                                        continue
                                    else:
                                        break
                                l2.remove(x1)

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x1:
                                            l[i][j]='o'

                                grid()

                                c2=check_3()
                                if c2=='':
                                    c1=check_2()
                                    if c1=='':
                                        if y=='bl':
                                            x='tl'
                                        elif y=='br':
                                            x='tr'
                                    else:
                                        x=c1
                                else:
                                    x=c2

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x:
                                            l[i][j]='x'
                                l2.remove(x)
                                
                                grid()
                                print(f"I have put x at {x}")

                                while True:
                                    x1=str(input(f"Where do you want to put o?"))
                                    if x1 not in l2:
                                        print("Invalid input")
                                        continue
                                    else:
                                        break

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x1:
                                            l[i][j]='o'
                                print(l2)
                                l2.remove(x1)

                                grid()

                                c=check_3()
                                if c=='':
                                    c=check_2()
                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==c:
                                            l[i][j]='x'
                                l2.remove(c)

                                grid()
                                print(f"I have put x at {c}")

                                k=check_1()
                                if k=='o':
                                    print("You won!!")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='x':
                                    print("I won!!")
                                    print("≧◔◡◔≦")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='':
                                    if l2==[]:
                                        print("Draw!!")
                                        if ch0=='4':
                                            print()
                                            print(f"Difficulty: {dd}")
                                        break
                        
                        else:
                            m=0
                            while True:
                                m+=1
                                if m==1:
                                    x=random.choice(l2)
                                else:
                                    x=check_2()
                                    if x=='':
                                        x=random.choice(l2)

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x:
                                            l[i][j]='x'
                                l2.remove(x)

                                grid()
                                print(f"I have put x at {x}")

                                k=check_1()
                                if k=='o':
                                    print("You won!!")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='x':
                                    print("I won!!")
                                    print("≧◔◡◔≦")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='':
                                    if l2==[]:
                                        print("Draw!!")
                                        if ch0=='4':
                                            print()
                                            print(f"Difficulty: {dd}")
                                        break
                                
                                while True:
                                    x1=str(input(f"Where do you want to put o?"))
                                    if x1 not in l2:
                                        print("Invalid input")
                                        continue
                                    else:
                                        break
                                l2.remove(x1)

                                for i in range(3):
                                    for j in range(3):
                                        if l1[i][j]==x1:
                                            l[i][j]='o'
                                
                                grid()

                                k=check_1()
                                if k=='o':
                                    print("You won!!")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='x':
                                    print("I won!!")
                                    print("≧◔◡◔≦")
                                    if ch0=='4':
                                        print()
                                        print(f"Difficulty: {dd}")
                                    break
                                elif k=='':
                                    if l2==[]:
                                        print("Draw!!")
                                        if ch0=='4':
                                            print()
                                            print(f"Difficulty: {dd}")
                                        break

                elif p=='x':
                    print("You will start!")
                    i=0
                    l3=['tl','tr','bl','br']  
                    while True:
                        i+=1
                        while True:
                            x1=str(input("Where do you want to put x?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)
                        if x1 in l3:
                            l3.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='x'      

                        grid()

                        k=check_1()
                        if k=='x':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='o':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break
                        
                        if i!=1:
                            j=check_2()
                    
                            if j=='':
                                if len(l3)==2:
                                    if l3[0][0]!=l3[1][0] and l3[0][1]!=l3[1][1]:
                                        while True:
                                            x=random.choice(l2)
                                            if x in l3:
                                                continue
                                            else:
                                                break
                                        l2.remove(x)
                                    else:
                                        x=random.choice(l2)
                                        l2.remove(x)

                                else:
                                    if 'mm' not in l2:
                                        if l3!=[]:
                                            if i==2:
                                                x=random.choice(l3)
                                                l3.remove(x)
                                            else:
                                                while True:
                                                    x=random.choice(l2)
                                                    if x in l3:
                                                        continue
                                                    else:
                                                        break
                                            l2.remove(x)

                                        else:
                                            x=random.choice(l2)
                                            l2.remove(x)
                                            if x in l3:
                                                l3.remove(x)

                                    else:
                                        x='mm'
                                        l2.remove(x)

                            else:
                                x=j
                                l2.remove(x)
                                if x in l3:
                                    l3.remove(x)
                        
                        else:
                            o=[]
                            for i in range(3):
                                for j in range(3):
                                    if l[i][j]==c:
                                        o.append(l1[i][j])
                            o1=o[0][0]+o[1][1]
                            o2=o[0][1]+o[1][0]
                            
                            for k in [o1,o2]:
                                if k in l3:
                                    x=k
                            
                            l2.remove(x)
                            if x in l3:
                                l3.remove(x)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x:
                                    l[i][j]='o'

                        grid()
                        print(f"I have put o at {x}")

                        k=check_1()
                        if k=='x':
                            print("You won!!")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='o':
                            print("I won!!")
                            print("≧◔◡◔≦")
                            if ch0=='4':
                                print()
                                print(f"Difficulty: {dd}")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                if ch0=='4':
                                    print()
                                    print(f"Difficulty: {dd}")
                                break
                break

            else:
                print("Invalid Input!!!")
                continue


        elif n=='2':
            n1=input("What is the name of the player who has x?")
            n2=input("What is the name of the player who has o?")
            print(f"Therefore {n1} will start!")
            while True:
                while True:
                    p1=input(f"Where do you want to put x,{n1}?")
                    if p1 in l2:
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==p1:
                                    l[i][j]='x'
                                    l2.remove(p1)
                        break
                    else:
                        print("Invalid Input!")
                        continue

                grid()

                k=check_1()
                if k=='o':
                    print(f"{n2} won!!")
                    break
                elif k=='x':
                    print(f"{n1} won!!")
                    break
                elif k=='':
                    if l2==[]:
                        print("Draw!!")
                        break
                    
                while True:
                    p2=input(f"Where do you want to put o,{n2}?")
                    if p2 in l2:
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==p2:
                                    l[i][j]='o'
                                    l2.remove(p2)
                        break
                    else:
                        print("Invalid Input!")
                        continue
                
                grid()

                k=check_1()
                if k=='o':
                    print(f"{n2} won!!")
                    break
                elif k=='x':
                    print(f"{n1} won!!")
                    break
                elif k=='':
                    if l2==[]:
                        print("Draw!!")
                        break

        else:
            print("Only 1 or 2 players can play :)")
            continue
        
        break
ttt()