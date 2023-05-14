import requests
import random
from tkinter import *
from time import sleep
import datetime
import os 
import math
import msvcrt 
import wolframalpha
import pywhatkit as pk

win = Tk()

def guiwindow():
    win.geometry("1107x215")
    win.configure(background='#869dda')
    win.title('Project Menu')
    btn1 = Button(win, text="Trick", command=magictrick,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn1.place(x = 50 , y = 30)
    btn2 = Button(win, text="Obstruction", command=obstr,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn2.place(x = 30, y = 90)
    btn3= Button(win, text="Calc", command=calculator,padx=20, pady =5,bg='#112d77',fg='#57ffae')#
    btn3.place(x = 50 , y = 150)
    btn4 = Button(win, text="TTT", command=ttt,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn4.place(x = 200 , y = 30)
    btn5 = Button(win, text="Battleship", command=battleship,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn5.place(x = 180 , y = 90)
    btn6 = Button(win, text="Puzzle", command=puzzle,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn6.place(x = 190, y = 150)
    btn7 = Button(win, text="TenTacToe", command=tentactoe,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn7.place(x = 330 , y = 30)
    btn8 = Button(win, text="DropDead", command=dropdead,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn8.place(x = 333 , y = 90)
    btn9 = Button(win, text="Gulam Chor", command=gulam_chor,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn9.place(x = 328, y = 150)
    btn10= Button(win, text="Memory", command=memory,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn10.place(x = 660 , y = 30)
    btn11= Button(win, text="Mastermind", command=mastermind,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn11.place(x = 490 , y = 90)
    btn12 = Button(win, text="S&L", command=snl,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn12.place(x = 515 , y = 150)
    btn13 = Button(win, text="PaswdGen", command=paswdgen,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn13.place(x = 495, y = 30)
    btn14 = Button(win, text="SOS", command=sos,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn14.place(x = 675 , y = 90)
    btn15 = Button(win, text="RPS", command=rps,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn15.place(x = 675 , y = 150)
    btn16 = Button(win, text="OddEven", command=oddeven,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn16.place(x = 800 , y = 30)
    btn17= Button(win, text="NumGuess", command=numguesser,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn17.place(x = 790 , y = 90)
    btn18 = Button(win, text="Research", command=yt_ggl,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn18.place(x = 800 , y = 150)
    btn19 = Button(win, text="FootBall", command=football,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn19.place(x = 960 , y = 30)
    btn20 = Button(win, text="Time", command=timepy,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn20.place(x = 970, y = 90)
    btn21 = Button(win, text="blackjack", command=exit_button,padx=20, pady =5,bg='#112d77',fg='#57ffae')
    btn21.place(x = 960, y = 150)
    win.mainloop()

def yt_ggl():
    wtd = input("what would u like to do -\n-> yt - open the browser and play the most relevant video according to your query.\n-> ggl - opens the browser and shows results for your query.\n-> w - Shows the weather status of the city u enter\n-> ")
    if wtd == 'yt':
        ytbe = input("what shoulod i search for?\n-> ")
        pk.playonyt(ytbe)
    elif wtd =='ggl':
        ggle = input("what should i search for?\n-> ")
        pk.search(ggle)
    elif wtd == 'w':
        city = input("Enter city name: ")
        owapik = str('9cd52d092a8769367d256b35c44d477f')
        url=str(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={owapik}')
        response = requests.get(url)
        x=response.json()
        print(x)
        if x["cod"] != "404":
            y=x['main']
            a = y['temp']
            temp = math.floor((a-273))
            coordlon = x['coord']['lon']
            coordlat = x['coord']['lat']
            statement1=x['weather'][0]['main']
            statement2 = x['weather'][0]['description']
            mt=y['feels_like']
            mintemp=math.floor((mt-273))
            p=y['pressure']
            pressure = math.floor((p//100))
            humidity = y['humidity']
            visibility=x['visibility']
            windspeed = x['wind']['speed']
            winddeg = x['wind']['deg']
            ctemp = (temp+mintemp)//2
            statement = f'''
            Temperature = {temp}
            Coords(latitude) = {coordlat}
            Coords(longitude) = {coordlon}
            Statements  = {statement1},{statement2}
            Feels like = {mt}
            Min(temp) = {mintemp}
            Pressure = {pressure}
            Humidity =  {humidity}
            Vsiibility = {visibility}
            Wind speed = {windspeed}
            Wind Deg = {winddeg}
            '''
            print(statement)
    else:
        print("invalid input")
        
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
        os.system('clear')
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

def calculator():
    os.system('cls')
    print()
    wtd = input("What would u like to do:\n\n-> h - View history (latest 10 queries)\n-> q - Run a query (max 15 characters)\n-> e - exit\n\n- ")
    if wtd == 'q':
        print()
        question = input('Enter your query:\n')
        app_id = '7QRP2U-RKGE22GQGY'
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print("Answer - ",answer)
        with open("calculator.txt",'a+') as calc:
            calc.write("Q - "+str(question)+' , '+"A - "+str(answer)+'\n')
        print("Q & A added to history")
    elif wtd == 'h':
        with open("calculator.txt",'r+') as calc:
            history = calc.readlines()
            if len(history)>10:
                for j in range(0,10):
                    a = history[j]
                    if '\n' in history[j]:
                        print(a[:-1])
                    else:
                        print(a)
            else:
                for j in range(0,len(history)):
                    a = history[j]
                    if '\n' in history[j]:
                        print(a[:-1])
                    else:
                        print(a)         
    else:
        print("code has been exited")
        exit()

def timepy():

    #Alarm

    def a():
        os.system('cls')
        t2=input("Enter time:").lower()

        if t2[-2:] in ('am','pm'):
            t1=t2[:-3]
        else:
            t1=t2

        a=t1.split(':')
        if a[0] in ['1','2','3','4','5','6','7','8','9','10','11','12']:
            if a[0] in ['1','2','3','4','5','6','7','8','9']:
                t='0'+t1+':00'
            if t2[-2:]=='pm':
                t=str(12+int(a[0]))+':'+a[1]+':00'
        else:
            t=t1+':00'

        while True:
            d=datetime.datetime.now()
            d1=str(d)
            l=d1.split(' ')
            l1=l[1].split('.')
            t1=l1[0]
            if t1==t:
                os.system("start alarm_sound.mp3")
                print("IT'S TIME!!!")
                break

    #Stopwatch

    def s():
        os.system('cls')
        x='stop'

        print("Press s to start!")

        while True:
            if msvcrt.kbhit():
                w=msvcrt.getch()
                p=str(w)
                k=p[-2]
                if k=='s':
                    x='start'
                    break
                else:
                    print("PRESS s!!!")

        sleep(1)
        h,m,s=0,0,0
        print("Stopwatch has started!")
        print("Press s to stop and p to pause!")
        while x=='start':
            s+=1
            sleep(1)
            os.system("cls")
            if s==60:
                m+=1
                s=0
                if m==60:
                    h+=1
                    m=0
            print('\n'*6)
            print(' '*23,'STOPWATCH')
            print(' '*25,end='')
            if s>=10:
                print(' ------')
            else:
                print(' -----')
            print(' '*25,end='')
            print(f"|{h}:{m}:{s}|")
            print(' '*25,end='')
            if s>=10:
                print(' ------')
            else:
                print(' -----')
            if msvcrt.kbhit():
                w=msvcrt.getch()
                p=str(w)
                k=p[-2]
                if k=='s':
                    x='stop'
                elif k=='p':
                    print("Press p to resume!")
                    while True:
                        if msvcrt.kbhit():
                            w=msvcrt.getch()
                            p=str(w)
                            k=p[-2]
                            if k=='p':
                                break

        print("Stopwatch has ended!")
        print(f"Time: {h} hours, {m} minutes and {s} seconds")

    #Timer

    def t():
        os.system('cls')

        h=int(input("Enter hours:"))
        m=int(input("Enter minutes:"))
        s=int(input("Enter seconds:"))

        print("Press p to pause!")
        sleep(2)

        os.system("cls")

        x=h*3600+m*60+s

        for i in range(x,0,-1):
            os.system("cls")
            print('\n'*6)
            print(' '*21,end='')
            print("TIMER")
            print(' '*20,end='')
            if s>=10:
                print(' ------')
            else:
                print(' -----')
            print(' '*20,end='')
            print(f"|{h}:{m}:{s}|")
            print(' '*20,end='')
            if s>=10:
                print(' ------')
            else:
                print(' -----')
            sleep(1)
            os.system("cls")
            if s!=0:
                s-=1
            else:
                if m!=0:
                    m-=1
                    s=59
                else:
                    if h!=0:
                        h-=1
                        m=59

            while True:
                if msvcrt.kbhit():
                    w=msvcrt.getch()
                    p=str(w)
                    k=p[-2]
                    if k=='p':
                        print('\n'*6)
                        print(' '*21,end='')
                        print("TIMER")
                        print(' '*20,end='')
                        if s>=10:
                            print(' ------')
                        else:
                            print(' -----')
                        print(' '*20,end='')
                        print(f"|{h}:{m}:{s}|")
                        print(' '*20,end='')
                        if s>=10:
                            print(' ------')
                        else:
                            print(' -----')
                        print("Press p to resume!")
                        while True:
                            if msvcrt.kbhit():
                                w=msvcrt.getch()
                                p=str(w)
                                k=p[-2]
                                if k=='p':
                                    break
                else:
                    break                

        os.system("start timer_sound.wav")
        print("TIMER OVER!!!")

    #Clock
    def c():
        while True:
            sleep(1)
            k=str(datetime.datetime.now())
            l=k.split()
            l1=l[1].split('.')
            t=l1[0]

            os.system('cls')
            
            print('\n'*3)
            print('\t'*2,' ',"CLOCK")
            print('\t'*2,end=' ')
            print(' --------',end='\n')
            print('\t'*2,end='')
            print(' |',end='')
            print(t,end='')
            print('|')
            print('\t'*2,end=' ')
            print(' --------',end='\n')
    wtd = input("What would you like to do?\n-> a - Set an alarm\n-> c - View the clock in realtime on your terminal\n-> s - Stopwatch\n-> t - Set a timer\n-> ")
    if wtd == 'a':
        a()
    elif wtd == 'c':
        c()
    elif wtd == 's':
        s()
    elif wtd == 't':
        t()
    else:
        print("invalid input")

def battleship():
    print("We are playing Battleship!!!")
    print("Rules of the game are very simple. There will be a 5X5 grid, in which 10 battleships will be placed on random positions and you have to destroy them and complete with the computer. You have to guess the postion of battleships and if you get them right then you destroy that battleship. After all the battleships are destroyed then the one who destroyed more than the other wins!!!")

    BS=[]

    PBCount=0
    CBCount=0

    alpha=['a','b','c','d','e','f']

    a1='   '
    a2='   '
    a3='   '
    a4='   '
    a5='   '
    b1='   '
    b2='   '
    b3='   '
    b4='   '
    b5='   '
    c1='   '
    c2='   '
    c3='   '
    c4='   '
    c5='   '
    d1='   '
    d2='   '
    d3='   '
    d4='   '
    d5='   '
    e1='   '
    e2='   '
    e3='   '
    e4='   '
    e5='   '
    f1='   '
    f2='   '
    f3='   '
    f4='   '
    f5='   '
    l=[[a1,a2,a3,a4,a5],[b1,b2,b3,b4,b5],[c1,c2,c3,c4,c5],[d1,d2,d3,d4,d5],[e1,e2,e3,e4,e5],[f1,f2,f3,f4,f5]]
    l1=[['a1','a2','a3','a4','a5'],['b1','b2','b3','b4','b5'],['c1','c2','c3','c4','c5'],['d1','d2','d3','d4','d5'],['e1','e2','e3','e4','e5'],['f1','f2','f3','f4','f5']]
    l2=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5','f1','f2','f3','f4','f5']

    print("Positions:")
    print("      1       2       3       4       5    ")
    print("  +-------+-------+-------+-------+-------+")
    print("a |  ",l1[0][0]," |  ",l1[0][1]," |  ",l1[0][2]," |  ",l1[0][3]," |  ",l1[0][4]," |")
    print("  +-------+-------+-------+-------+-------+")
    print("b |  ",l1[1][0]," |  ",l1[1][1]," |  ",l1[1][2]," |  ",l1[1][3]," |  ",l1[1][4]," |")
    print("  +-------+-------+-------+-------+-------+")
    print("c |  ",l1[2][0]," |  ",l1[2][1]," |  ",l1[2][2]," |  ",l1[2][3]," |  ",l1[2][4]," |")
    print("  +-------+-------+-------+-------+-------+")
    print("d |  ",l1[3][0]," |  ",l1[3][1]," |  ",l1[3][2]," |  ",l1[3][3]," |  ",l1[3][4]," |")
    print("  +-------+-------+-------+-------+-------+")
    print("e |  ",l1[4][0]," |  ",l1[4][1]," |  ",l1[4][2]," |  ",l1[4][3]," |  ",l1[4][4]," |")
    print("  +-------+-------+-------+-------+-------+")
    print("f |  ",l1[5][0]," |  ",l1[5][1]," |  ",l1[5][2]," |  ",l1[5][3]," |  ",l1[5][4]," |")
    print("  +-------+-------+-------+-------+-------+")
    print()

    sleep(20)
    os.system('clear')

    for k in range(10):
        while True:
            r=random.choice(l2)
            if r not in BS:
                break
        BS.append(r)

    while True:
        print("      1       2       3       4       5    ")
        print("  +-------+-------+-------+-------+-------+")
        print("a | ",l[0][0]," | ",l[0][1]," | ",l[0][2]," | ",l[0][3]," | ",l[0][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("b | ",l[1][0]," | ",l[1][1]," | ",l[1][2]," | ",l[1][3]," | ",l[1][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("c | ",l[2][0]," | ",l[2][1]," | ",l[2][2]," | ",l[2][3]," | ",l[2][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("d | ",l[3][0]," | ",l[3][1]," | ",l[3][2]," | ",l[3][3]," | ",l[3][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("e | ",l[4][0]," | ",l[4][1]," | ",l[4][2]," | ",l[4][3]," | ",l[4][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("f | ",l[5][0]," | ",l[5][1]," | ",l[5][2]," | ",l[5][3]," | ",l[5][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print()

        print("Player:",PBCount,'  ',"Computer:",CBCount,'\n')

        print("YOUR TURN")
        i=input("Enter position:")
        i=i.lower()

        if len(i)!=2:
            print("Invalid Input!")
        else:
            if i[0] not in 'abcdef' or i[1] not in '12345':
                print("Invalid Input!")
                sleep(1)
                os.system('clear')
                continue
            else:
                if i not in l2:
                    print("Invaild Input!")
                    sleep(1)
                    os.system('clear')
                    continue
                else:
                    l2.remove(i)
                    if i not in BS:
                        for j in range(6):
                            for k in range(5):
                                if l1[j][k]==i:
                                    l[j][k]=' X '
                    else:    
                        for j in range(6):
                            for k in range(5):
                                if l1[j][k]==i:
                                        l[j][k]=' BS'

                    print("      1       2       3       4       5    ")
                    print("  +-------+-------+-------+-------+-------+")
                    print("a | ",l[0][0]," | ",l[0][1]," | ",l[0][2]," | ",l[0][3]," | ",l[0][4]," |")
                    print("  +-------+-------+-------+-------+-------+")
                    print("b | ",l[1][0]," | ",l[1][1]," | ",l[1][2]," | ",l[1][3]," | ",l[1][4]," |")
                    print("  +-------+-------+-------+-------+-------+")
                    print("c | ",l[2][0]," | ",l[2][1]," | ",l[2][2]," | ",l[2][3]," | ",l[2][4]," |")
                    print("  +-------+-------+-------+-------+-------+")
                    print("d | ",l[3][0]," | ",l[3][1]," | ",l[3][2]," | ",l[3][3]," | ",l[3][4]," |")
                    print("  +-------+-------+-------+-------+-------+")
                    print("e | ",l[4][0]," | ",l[4][1]," | ",l[4][2]," | ",l[4][3]," | ",l[4][4]," |")
                    print("  +-------+-------+-------+-------+-------+")
                    print("f | ",l[5][0]," | ",l[5][1]," | ",l[5][2]," | ",l[5][3]," | ",l[5][4]," |")
                    print("  +-------+-------+-------+-------+-------+")
                    print()
                    
                    if i in BS:
                        print("You destroyed a battleship!!")
                        BS.remove(i)
                        PBCount+=1

                    print("Player:",PBCount,'  ',"Computer:",CBCount,'\n')

        sleep(3)
        os.system('clear')
        
        if BS==[]:
            print("ALL BATTLESHIPS ARE DESTROYED!!!")
            if PBCount>CBCount:
                print("YOU WON!!!")
            elif PBCount<CBCount:
                print("I WON!!!")
            else:
                print("TIE!!!")
            break

        print("MY TURN")

        i=random.choice(l2)

        l2.remove(i)

        if i not in BS:
            for j in range(6):
                for k in range(5):
                    if l1[j][k]==i:
                        l[j][k]=' / '
        else:    
            for j in range(6):
                for k in range(5):
                    if l1[j][k]==i:
                            l[j][k]=' BS'

        print("      1       2       3       4       5    ")
        print("  +-------+-------+-------+-------+-------+")
        print("a | ",l[0][0]," | ",l[0][1]," | ",l[0][2]," | ",l[0][3]," | ",l[0][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("b | ",l[1][0]," | ",l[1][1]," | ",l[1][2]," | ",l[1][3]," | ",l[1][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("c | ",l[2][0]," | ",l[2][1]," | ",l[2][2]," | ",l[2][3]," | ",l[2][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("d | ",l[3][0]," | ",l[3][1]," | ",l[3][2]," | ",l[3][3]," | ",l[3][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("e | ",l[4][0]," | ",l[4][1]," | ",l[4][2]," | ",l[4][3]," | ",l[4][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("f | ",l[5][0]," | ",l[5][1]," | ",l[5][2]," | ",l[5][3]," | ",l[5][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print()
        
        print("I entered position",i)

        if i in BS:
            print("I destroyed a battleship!!")
            BS.remove(i)
            CBCount+=1

        print("Player:",PBCount,'  ',"Computer:",CBCount,'\n')

        if BS==[]:
            print("ALL BATTLESHIPS ARE DESTROYED!!!")
            if PBCount>CBCount:
                print("YOU WON!!!")
            elif PBCount<CBCount:
                print("I WON!!!")
            else:
                print("TIE!!!")
            break

        sleep(3)
        os.system('clear')

def puzzle():
    os.system('cls')

    print("Can you solve this puzzle?")
    print("You can use arrow keys or w, a, s and d keys for the movement of the pieces.")
    sleep(5)

    l0=[' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10',' 11',' 12',' 13',' 14',' 15','   ']
    l1=[[' 1 ',' 2 ',' 3 ',' 4 '],[' 5 ',' 6 ',' 7 ',' 8 '],[' 9 ',' 10',' 11',' 12'],[' 13',' 14',' 15','   ']]

    random.shuffle(l0)

    p11=l0[0]
    p12=l0[1]
    p13=l0[2]
    p14=l0[3]
    p21=l0[4]
    p22=l0[5]
    p23=l0[6]
    p24=l0[7]
    p31=l0[8]
    p32=l0[9]
    p33=l0[10]
    p34=l0[11]
    p41=l0[12]
    p42=l0[13]
    p43=l0[14]
    p44=l0[15]

    l=[[p11,p12,p13,p14],[p21,p22,p23,p24],[p31,p32,p33,p34],[p41,p42,p43,p44]]

    def grid(l):
        os.system('cls')
        print('\n'*2)
        for i in range(4):
            print('\t',end='')
            print('+',end='')
            print('-----+'*4)
            print('\t',end='')
            print('|',end='')
            for j in range(4):
                print(f' {l[i][j]} |',end='')
            print()
        print('\t',end='')
        print('+',end='')
        print('-----+'*4)

    grid(l)

    ll=[]
    while True:
        c=0
        while True:
            if msvcrt.kbhit():
                n=0
                while True:
                    n+=1
                    s=msvcrt.getch()
                    p=str(s)
                    k=str(p[-2])
                    if "b'\\x00'" in p:
                        if n==2:
                            break
                    else:
                        break
                break

        if k in ('s','P'):
            if '   ' not in l[0]:
                for i in range(4):
                    for j in range(4):
                        if l[i][j]=='   ' and c==0:
                            l[i-1][j],l[i][j]=l[i][j],l[i-1][j]
                            c=1
        elif k in ('d','M'):
            if '   ' not in [l[0][0],l[1][0],l[2][0],l[3][0]]:
                for i in range(4):
                    for j in range(4):
                        if l[i][j]=='   ' and c==0:
                            l[i][j-1],l[i][j]=l[i][j],l[i][j-1]
                            c=1
        elif k in ('w','H'):
            if '   ' not in l[-1]:
                for i in range(4):
                    for j in range(4):
                        if l[i][j]=='   ' and c==0:
                            l[i+1][j],l[i][j]=l[i][j],l[i+1][j]
                            c=1
        elif k in ('a','K'):
            if '   ' not in [l[0][-1],l[1][-1],l[2][-1],l[3][-1]]:
                for i in range(4):
                    for j in range(4):
                        if l[i][j]=='   ' and c==0:
                            l[i][j+1],l[i][j]=l[i][j],l[i][j+1]
                            c=1
        else:
            if k!="0":
                print("Invaild Input!!!")
                sleep(0.5)
        
        grid(l)

        if l==l1:
            l1[-1][-1]=' 16'
            grid(l1)
            print("\nPUZZLE COMPLETED!!!")
            break

def magictrick():
    original_card_list = ["clubs_king","hearts_king","spades_king","diamonds_king","clubs_queen","hearts_queen","spades_queen","diamonds_queen"]
    colors = {"spades":"black","clubs":"black","hearts":"red","diamonds":"red"}
    original_card_list1 = [1,2,3,4,5,6,7,8]
    left_cards = []
    right_cards = []

    print()
    print(original_card_list)
    print()
    print("Choose a card from the above list , you dont have to tell me :) ")
    print()
    chosen = input("Did you choose a card?\n")
    print()
    print("okay , lets start then")
    print()

    for i in original_card_list:
        if original_card_list.index(i)%2==0:
            right_cards.append(i)
        else:
            left_cards.append(i)
            
    print("Cards to show - ",left_cards)
    print()
    question1 = input("Do you see your chosen card in this?\n")

    if question1=='y':
        original_card_list = right_cards+left_cards
    else:
        original_card_list = left_cards+right_cards
    os.system("clear")
    #os.system("cls")

    left_cards = []
    right_cards = []
    for i in original_card_list:
        if original_card_list.index(i)%2==0:
            left_cards.append(i)
        else:
            right_cards.append(i)
            
    left_cards.reverse()
    right_cards.reverse()
    print("Cards to show - ",left_cards)
    print()
    question2 = input("Do you see your chosen card in this?\n")

    if question2=='y':
        original_card_list = left_cards+right_cards
    else:
        original_card_list = right_cards+left_cards
        
    os.system("clear")
    #os.system("cls")
    left_cards = []
    right_cards = []
    for i in original_card_list:
        if original_card_list.index(i)%2==0:
            right_cards.append(i)
        else:
            left_cards.append(i)
            
    print("Cards to show - ",left_cards)
    print()
    question2 = input("Do you see your chosen card in this?\n")

    if question2=='y':
        original_card_list = left_cards+right_cards
    else:
        original_card_list = right_cards+left_cards
    os.system("clear")

    #os.system("cls")
    list1 =[]
    list2=[]
    list3=[]
    b = ''
    a = ''

    for i in original_card_list:
        if original_card_list.index(i)%2==0:
            list1.append(i)
        else:
            list2.append(i)
    for i in list1:
        if list1.index(i)%2==0:
            list3.append(i)
            
    d = list3[1]
    e = d.split("_")
    ee = e[0]
    a = list3[0]
    sleep(2)
    aa = list2[0].split("_")

    print("The gender of your card is -",aa[1])
    sleep(2)
    zz = list1[0]
    bb = zz.split("_")
    cc = bb[0]
    dd = colors[f"{cc}"]
    print("the color of your card is -",dd)
    sleep(2)
    print("the suit of your card is -",ee)
    sleep(2)
    print("Hence the card you chose was -",a)

def obstr():
    obs = {'a1':'a2,b2,b1','a2':'a1,a3,b1,b2,b3','a3':'a2,a4,b2,b3,b4','a4':'a3,a5,b3,b4,b5','a5':'a4,a6,b4,b5,b6','a6':'a5,b5,b6',
        'b1':'a1,a2,b2,c2,c1','b2':'a1,a2,a3,b1,b3,c1,c2,c3','b3':'a2,a3,a4,b2,b4,c2,c3,c4','b4':'a3,a4,a5,b3,b5,c3,c4,c5','b5':'a4,a5,a6,b4,b6,c4,c5,c6','b6':'a6,a5,b5,c5,c6',
        'c1':'b1,b2,c2,d1,d2','c2':'b1,b2,b3,c1,c3,d1,d2,d3','c3':'b2,b3,b4,c2,c4,d2,d3,d4','c4':'b3,b4,b5,c3,c5,d3,d4,d5','c5':'b4,b5,b6,c4,c6,d4,d5,d6','c6':'b6,b5,c5,d5,d6',
        'd1':'c1,c2,d2,e1,e2','d2':'d1,c2,c3,c1,d3,e1,e2,e3','d3':'c2,c3,c4,d2,d4,e2,e3,e4','d4':'c3,c4,c5,d3,d5,e3,e4,e5','d5':'c4,c5,c6,d4,d6,e4,e5,e6','d6':'c6,c5,d5,e5,e6',
        'e1':'d1,d2,e2,f1,f2','e2':'d1,d2,d3,e1,e3,f1,f2,f3','e3':'d2,d3,d4,e2,e4,f2,f3,f4','e4':'d3,d4,d5,e3,e5,f3,f4,f5','e5':'d4,d5,d6,e4,e6,f4,f5,f6','e6':'d6,d5,e5,f5,f6',
        'f1':'e1,e2,f2','f2':'f1,e1,e2,e3,f3','f3':'f2,e2,e3,e4,f4','f4':'f3,e3,e4,e5,f5','f5':'f4,e4,e5,e6,f6','f6':'f5,e5,e6'}
    l1=['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6','c1','c2','c3','c4','c5','c6','d1','d2','d3','d4','d5','d6','e1','e2','e3','e4','e5','e6','f1','f2','f3','f4','f5','f6']
    l2=['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6','c1','c2','c3','c4','c5','c6','d1','d2','d3','d4','d5','d6','e1','e2','e3','e4','e5','e6','f1','f2','f3','f4','f5','f6']
    print("Its the players turn")
    print()
    print("+------+------+------+------+------+------+")
    print("| ",l1[0]," | ",l1[1]," | ",l1[2]," | ",l1[3]," | ",l1[4]," | ",l1[5]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[6]," | ",l1[7]," | ",l1[8]," | ",l1[9]," | ",l1[10]," | ",l1[11]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[12]," | ",l1[13]," | ",l1[14]," | ",l1[15]," | ",l1[16]," | ",l1[17]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[18]," | ",l1[19]," | ",l1[20]," | ",l1[21]," | ",l1[22]," | ",l1[23]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[24]," | ",l1[25]," | ",l1[26]," | ",l1[27]," | ",l1[28]," | ",l1[29]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[30]," | ",l1[31]," | ",l1[32]," | ",l1[33]," | ",l1[34]," | ",l1[35]," |")
    print("+------+------+------+------+------+------+")
    print()
    while True:
        if len(l2)==0:
            print("You have lost to the AI in a fair match , lol")
            break  
        else:
            x=input("Where do you want to put the X? , look at the grid and enter accordingly: \n")
            aa = obs[f'{x}']
            if x in l2:
                l2.remove(x)
                bb = aa.split(',')
                a = str(l1).replace(f'{x}','XX')
                b = str(a).replace("'",'') 
                c = str(b).replace('[','')
                d = str(c).replace(']','')
                e = str(d).replace(" ","")

                for j in bb:
                    if j in e:
                        l2.remove(j)
                        e = e.replace(j,"//")
                        continue
                l1=e.split(',')
                print("+------+------+------+------+------+------+")
                print("| ",l1[0]," | ",l1[1]," | ",l1[2]," | ",l1[3]," | ",l1[4]," | ",l1[5]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[6]," | ",l1[7]," | ",l1[8]," | ",l1[9]," | ",l1[10]," | ",l1[11]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[12]," | ",l1[13]," | ",l1[14]," | ",l1[15]," | ",l1[16]," | ",l1[17]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[18]," | ",l1[19]," | ",l1[20]," | ",l1[21]," | ",l1[22]," | ",l1[23]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[24]," | ",l1[25]," | ",l1[26]," | ",l1[27]," | ",l1[28]," | ",l1[29]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[30]," | ",l1[31]," | ",l1[32]," | ",l1[33]," | ",l1[34]," | ",l1[35]," |")
                print("+------+------+------+------+------+------+")
            else:
                print("illegal move : that Grid element is already occupied")
                print("Your turn is now skipped for that")
        if len(l2)==0:
            print("The AI has lost in a fair match , GG")
            break 
        else:
            z = random.choice(l2)
            nn = obs[f'{z}']
            l2.remove(z)
            mm = nn.split(',')
            p = str(l1).replace(f'{z}','OO')
            q = str(p).replace("'",'') 
            r = str(q).replace('[','')
            s = str(r).replace(']','')
            t = str(s).replace(" ","")
            for u in mm:
                if u in t:
                    l2.remove(u)
                    t = t.replace(u,"::")
                    continue
            l1=t.split(',')
            print()
            print("+------+------+------+------+------+------+")
            print("| ",l1[0]," | ",l1[1]," | ",l1[2]," | ",l1[3]," | ",l1[4]," | ",l1[5]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[6]," | ",l1[7]," | ",l1[8]," | ",l1[9]," | ",l1[10]," | ",l1[11]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[12]," | ",l1[13]," | ",l1[14]," | ",l1[15]," | ",l1[16]," | ",l1[17]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[18]," | ",l1[19]," | ",l1[20]," | ",l1[21]," | ",l1[22]," | ",l1[23]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[24]," | ",l1[25]," | ",l1[26]," | ",l1[27]," | ",l1[28]," | ",l1[29]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[30]," | ",l1[31]," | ",l1[32]," | ",l1[33]," | ",l1[34]," | ",l1[35]," |")
            print("+------+------+------+------+------+------+")
            print()  
            continue 
    obstr()

def football():

    print("Let's play football without football!!!")

    while True:
        x=input("Choose foot or ball>")
        if x=='foot':
            print("Therefore I have ball!")
            break
        elif x=='ball':
            print("Therefore I have foot!")
            break
        else:
            print("Invalid Input!!")
            continue

    n=int(input("Enter a number between 1 to 10:"))
    n1=random.randint(1,10)
    print("I took out",n1)

    pl=''
    cm=''

    pgoals=0
    cgoals=0

    if x.lower()=='foot':
        if (n+n1)%2==0:
            r=random.choice(['Center','Side'])
            print(f"I won, therefore I choose {r}!!")
            for i in ['Center','Side']:
                if i!=r:
                    print(f"Therefore you have {i}!!")
            if r=='Center':
                cm='ball'
            else:
                pl='ball'
        else:
            print("You won!!")
            y=input("Choose center or side>")
            if y.lower()=='center':
                print("Therfore I have side!!")
                pl='ball'
            elif y.lower()=='side':
                print("Therefore I have center!!")
                cm='ball'
    else:
        if (n+n1)%2==0:
            print("You won!!")
            y=input("Choose center or side>")
            if y.lower()=='center':
                print("Therfore I have side!!")
                pl='ball'
            elif y.lower()=='side':
                print("Therefore I have center!!")
                cm='ball'
        else:
            r=random.choice(['Center','Side'])
            print(f"I won, therefore I choose {r}!!")
            for i in ['Center','Side']:
                if i!=r:
                    print(f"Therefore you have {i}!!")
            if r=='Center':
                cm='ball'
            else:
                pl='ball'

    print("Let's start the match!!!")

    t=int(input("For how many goals do you want to play?"))
    n=0
    while True:
        n+=1
        p=int(input("Enter number:"))
        if p not in [1,2,3]:
            while True:
                print("PENELTY!!!")
                print("Enter 7, 8 or 9!!")
                k=int(input("Enter number:"))
                if k not in (7,8,9):
                    continue
                else:
                    r=random.randint(7,9)
                    print("My number:",r)
                    if k==r:
                        print("Goal Saved!!")
                    else:
                        print("GOAL!!!")
                        cgoals+=1
                    print("Your Score:",pgoals)
                    print("My Score:",cgoals)
                    pl,cm=cm,pl
                    if pgoals!=t and cgoals!=t:
                        if pl=='ball':
                            print("You have the ball now!!")
                        else:
                            print("I have the ball now!!")
                    n=0
                    break
            continue
        
        c=random.randint(1,3)
        print("My number:",c)

        if p!=c:
            print(f"Pass {n}")
            if n!=3:
                continue
        else:
            print("Tackled!!")
            n=0
            pl,cm=cm,pl
            if pl=='ball':
                print("You have the ball now!!")
            else:
                print("I have the ball now!!")
            continue

        if n==3:
            print("Goal Time!!")
            print("Enter 4, 5 or 6!!")
            g=int(input("Enter number:"))
            if g not in (4,5,6):
                while True:
                    print("PENELTY!!!")
                    print("Enter 7, 8 or 9!!")
                    k=int(input("Enter number:"))
                    if k not in (7,8,9):
                        continue
                    else:
                        r=random.randint(7,9)
                        print("My number:",r)
                        if k==r:
                            print("Goal Saved!!")
                        else:
                            print("GOAL!!!")
                            cgoals+=1
                        print("Your Score:",pgoals)
                        print("My Score:",cgoals)
                        pl,cm=cm,pl
                        if pgoals!=t and cgoals!=t:
                            if pl=='ball':
                                print("You have the ball now!!")
                            else:
                                print("I have the ball now!!")
                        n=0
                        break
                continue
            else:
                r=random.randint(4,6)
                print("My number:",r)
                if g==r:
                    print("Goal Saved!!")
                else:
                    print("GOAL!!!")
                    if pl=='ball':
                        pgoals+=1
                    else:
                        cgoals+=1
                print("Your Score:",pgoals)
                print("My Score:",cgoals)
                pl,cm=cm,pl
                if pgoals!=t and cgoals!=t:
                    if pl=='ball':
                        print("You have the ball now!!")
                    else:
                        print("I have the ball now!!")

        if pgoals==t:
            print("YOU WON!!!")
            break
        elif cgoals==t:
            print("I WON!!!")
            break
        
        n=0

def tentactoe():
    os.system('cls')
    print("Let's play Ten-Tac-Toe!!!")

    def check_1(t):
        ctr=0
        for i in range(3):
            if t[i][0]==t[i][1] and t[i][0]==t[i][2] and t[i][0]!=' ':
                ctr=1
                break
            elif t[0][i]==t[1][i] and t[0][i]==t[2][i] and t[0][i]!=' ':
                ctr=1
                break
            elif t[0][0]==t[1][1] and t[0][0]==t[2][2] and t[0][0]!=' ':
                ctr=1
                break
            elif t[0][2]==t[1][1] and t[0][2]==t[2][0] and t[0][2]!=' ':
                ctr=1
                break
        else:
            return False
        if ctr==1:
            return True

    def check_2(l):
        if l[0][0]==l[1][1] and l[2][2]==' ' and l[0][0]==p:
            return 2,2
        elif l[0][0]==l[2][2] and l[1][1]==' ' and l[0][0]==p:
            return 1,1
        elif l[1][1]==l[2][2] and l[0][0]==' ' and l[1][1]==p:
            return 0,0
        elif l[0][2]==l[1][1] and l[2][0]==' ' and l[0][2]==p:
            return 2,0
        elif l[0][2]==l[2][0] and l[1][1]==' ' and l[0][2]==p:
            return 1,1
        elif l[2][0]==l[1][1] and l[0][2]==' ' and l[2][0]==p:
            return 0,2
        else:
            r,s=-1,-1
            for i in range(3):
                if l[i][0]==l[i][1] and l[i][2]==' ' and l[i][0]==p:
                    r,s=i,2
                    break
                elif l[i][0]==l[i][2] and l[i][1]==' ' and l[i][0]==p:
                    r,s=i,1
                    break
                elif l[i][1]==l[i][2] and l[i][0]==' ' and l[i][1]==p:
                    r,s=i,0
                    break
                elif l[0][i]==l[1][i] and l[2][i]==' ' and l[0][i]==p:
                    r,s=2,i
                    break
                elif l[0][i]==l[2][i] and l[1][i]==' ' and l[0][i]==p:
                    r,s=1,i
                    break
                elif l[1][i]==l[2][i] and l[0][i]==' ' and l[1][i]==p:
                    r,s=0,i
                    break
            else:
                return None,None
            if (r!=-1 and s!=-1):
                return r,s

    def check_3(l):
        if l[0][0]==l[1][1] and l[2][2]==' ' and l[0][0]==c:
            return 2,2
        elif l[0][0]==l[2][2] and l[1][1]==' ' and l[0][0]==c:
            return 1,1
        elif l[1][1]==l[2][2] and l[0][0]==' ' and l[1][1]==c:
            return 0,0
        elif l[0][2]==l[1][1] and l[2][0]==' ' and l[0][2]==c:
            return 2,0
        elif l[0][2]==l[2][0] and l[1][1]==' ' and l[0][2]==c:
            return 1,1
        elif l[2][0]==l[1][1] and l[0][2]==' ' and l[2][0]==c:
            return 0,2
        else:
            r,s=-1,-1
            for i in range(3):
                if l[i][0]==l[i][1] and l[i][2]==' ' and l[i][0]==c:
                    r,s=i,2
                    break
                elif l[i][0]==l[i][2] and l[i][1]==' ' and l[i][0]==c:
                    r,s=i,1
                    break
                elif l[i][1]==l[i][2] and l[i][0]==' ' and l[i][1]==c:
                    r,s=i,0
                    break
                elif l[0][i]==l[1][i] and l[2][i]==' ' and l[0][i]==c:
                    r,s=2,i
                    break
                elif l[0][i]==l[2][i] and l[1][i]==' ' and l[0][i]==c:
                    r,s=1,i
                    break
                elif l[1][i]==l[2][i] and l[0][i]==' ' and l[1][i]==c:
                    r,s=0,i
                    break
            else:
                return None,None
            if (r!=-1 and s!=-1):
                return r,s

    tl=' '
    tm=' '
    tr=' '
    ml=' '
    mm=' '
    mr=' '
    bl=' '
    bm=' '
    br=' '

    ttt=[[tl,tm,tr],[ml,mm,mr],[bl,bm,br]]

    TL=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    TM=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    TR=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    ML=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    MM=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    MR=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    BL=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    BM=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    BR=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    l=[TL,TM,TR,ML,MM,MR,BL,BM,BR]
    ll=[[TL,TM,TR],[ML,MM,MR],[BL,BM,BR]]
    ll1=[['TL','TM','TR'],['ML','MM','MR'],['BL','BM','BR']]
    ll2=['TL','TM','TR','ML','MM','MR','BL','BM','BR']
    l1=['tl','tm','tr','ml','mm','mr','bl','bm','br']
    l2=[['tl','tm','tr'],['ml','mm','mr'],['bl','bm','br']]

    def grid():
        os.system('cls')
        print()
        print(ttt[0][0]," | ",ttt[0][1]," | ",ttt[0][2])
        print("---+-----+---")
        print(ttt[1][0]," | ",ttt[1][1]," | ",ttt[1][2])
        print("---+-----+---")
        print(ttt[2][0]," | ",ttt[2][1]," | ",ttt[2][2])
        print()
        print("                 ||                 ||                ")
        print(f"  {TL[0][0]}  |  {TL[0][1]}  |  {TL[0][2]}  ||  {TM[0][0]}  |  {TM[0][1]}  |  {TM[0][2]}  ||  {TR[0][0]}  |  {TR[0][1]}  |  {TR[0][2]}   ")
        print(f" ----+-----+---- || ----+-----+---- || ----+-----+----")
        print(f"  {TL[1][0]}  |  {TL[1][1]}  |  {TL[1][2]}  ||  {TM[1][0]}  |  {TM[1][1]}  |  {TM[1][2]}  ||  {TR[1][0]}  |  {TR[1][1]}  |  {TR[1][2]}   ")
        print(f" ----+-----+---- || ----+-----+---- || ----+-----+----")
        print(f"  {TL[2][0]}  |  {TL[2][1]}  |  {TL[2][2]}  ||  {TM[2][0]}  |  {TM[2][1]}  |  {TM[2][2]}  ||  {TR[2][0]}  |  {TR[2][1]}  |  {TR[2][2]}   ")
        print(f"=======================================================")
        print(f"  {ML[0][0]}  |  {ML[0][1]}  |  {ML[0][2]}  ||  {MM[0][0]}  |  {MM[0][1]}  |  {MM[0][2]}  ||  {MR[0][0]}  |  {MR[0][1]}  |  {MR[0][2]}   ")
        print(f" ----+-----+---- || ----+-----+---- || ----+-----+----")
        print(f"  {ML[1][0]}  |  {ML[1][1]}  |  {ML[1][2]}  ||  {MM[1][0]}  |  {MM[1][1]}  |  {MM[1][2]}  ||  {MR[1][0]}  |  {MR[1][1]}  |  {MR[1][2]}   ")
        print(f" ----+-----+---- || ----+-----+---- || ----+-----+----")
        print(f"  {ML[2][0]}  |  {ML[2][1]}  |  {ML[2][2]}  ||  {MM[2][0]}  |  {MM[2][1]}  |  {MM[2][2]}  ||  {MR[2][0]}  |  {MR[2][1]}  |  {MR[2][2]}   ")
        print(f"=======================================================")
        print(f"  {BL[0][0]}  |  {BL[0][1]}  |  {BL[0][2]}  ||  {BM[0][0]}  |  {BM[0][1]}  |  {BM[0][2]}  ||  {BR[0][0]}  |  {BR[0][1]}  |  {BR[0][2]}   ")
        print(f" ----+-----+---- || ----+-----+---- || ----+-----+----")
        print(f"  {BL[1][0]}  |  {BL[1][1]}  |  {BL[1][2]}  ||  {BM[1][0]}  |  {BM[1][1]}  |  {BM[1][2]}  ||  {BR[1][0]}  |  {BR[1][1]}  |  {BR[1][2]}   ")
        print(f" ----+-----+---- || ----+-----+---- || ----+-----+----")
        print(f"  {BL[2][0]}  |  {BL[2][1]}  |  {BL[2][2]}  ||  {BM[2][0]}  |  {BM[2][1]}  |  {BM[2][2]}  ||  {BR[2][0]}  |  {BR[2][1]}  |  {BR[2][2]}   ")
        print("                 ||                 ||                ")
        print()

    print()
    while True:
        s=input("Enter number of players playing:")
        if s in ('1','2'):
            break
        else:
            print("Only 1 or 2 player/s can play!")

    if s=='1':
        while True:
            p1=input("Choose x or o>")
            p=p1.lower()
            if p=='x':
                c='o'
                print("You have chosen x and therefore I have o")
                break
            elif p=='o':
                c='x'
                print("You have chosen o and therefore I have x")
                break
            else:
                print("Invaild Input!")
    else:
        n1=input("Enter name of the player with x:")
        n2=input("Enter name of the player with o:")

    print()
    print("Name of the cells are tl for top left, tm for top middle, tr for top right, ml for middle left, mm for middle middle, mr for middle right, bl for bottom left, bm for bottom middle, br for bottom right.")

    print()
    print(" TL","|","TM","|","TR")
    print("----+----+----")
    print(" ML","|","MM","|","MR")
    print("----+----+----")
    print(" BL","|","BM","|","BR")
    print()

    print("                 ||                 ||                ")
    print("  tl | tm  |  tl ||  tl |  tm |  tl ||  tl |  tm |  tl")
    print(" ----+-----+---- || ----+-----+---- || ----+-----+----")
    print("  ml | mm  |  mr ||  ml |  mm |  mr ||  ml |  mm |  mr")
    print(" ----+-----+---- || ----+-----+---- || ----+-----+----")
    print("  bl | bm  |  br ||  bl |  bm |  br ||  bl |  bm |  br")
    print("========================================================")
    print("  tl | tm  |  tl ||  tl |  tm |  tl ||  tl |  tm |  tl")
    print(" ----+-----+---- || ----+-----+---- || ----+-----+----")
    print("  ml | mm  |  mr ||  ml |  mm |  mr ||  ml |  mm |  mr")
    print(" ----+-----+---- || ----+-----+---- || ----+-----+----")
    print("  bl | bm  |  br ||  bl |  bm |  br ||  bl |  bm |  br")
    print("========================================================")
    print("  tl | tm  |  tl ||  tl |  tm |  tl ||  tl |  tm |  tl")
    print(" ----+-----+---- || ----+-----+---- || ----+-----+----")
    print("  ml | mm  |  mr ||  ml |  mm |  mr ||  ml |  mm |  mr")
    print(" ----+-----+---- || ----+-----+---- || ----+-----+----")
    print("  bl | bm  |  br ||  bl |  bm |  br ||  bl |  bm |  br")
    print("                 ||                 ||                ")
    print()
    print("For your reference(if you want)")
    print()

    sleep(5)

    print("Best of luck!!")
    print("Let the battle begin!!")

    if s=='1':
        if p=='x':
            grid()
            while True:
                x=input(f"Where do you want to put {p}?")
                if x.lower() in l1:
                    break
                else:
                    print("Invaild Input!!")
            n=1
        elif p=='o':
            i=random.randint(0,8)
            j=random.randint(0,2)
            k=random.randint(0,2)
            l[i][j][k]=c
            x=l2[j][k]
            ix=l1.index(x)
            n=0
            grid()
            print(f"I have put {c} at {l2[j][k]} of {ll2[i]}")

        while True:
            print("\nYOUR TURN")

            if n==1:
                ix=l1.index(x)
                n=0

            jj=0
            for t1 in range(3):
                for t2 in range(3):
                    if l2[t1][t2]==x:
                        if ttt[t1][t2]==' ':
                            jj=1
            
            if jj==1:
                while True:
                    r=0
                    x1=input(f"Where do you want to put {p}?")
                    if x1 not in l1:
                        print("Invaild Input!")
                        continue

                    for k in range(3):
                        for q in range(3):
                            if l2[k][q]==x1:
                                if l[ix][k][q]==' ':
                                    l[ix][k][q]=p
                                    r=1
                                else:
                                    print("Invaild Input!")
                    
                    if r==1:
                        break
            else:
                while True:
                    y=input(f"Where do you want to put {p}?")
                    ix=l1.index(y.lower())
                    y1=y.upper()
                    if y1 in ll2:
                        while True:
                            x1=input(f"Where do you want to put {p}?")
                            if x1.lower() in l1:
                                break
                            else:
                                print("Invaild Input!!")
                        break
                    else:
                        print("Invaild Input!!")
                
                for u in range(3):
                    for v in range(3):
                        if ll1[u][v]==y1:
                            for uu in range(3):
                                for vv in range(3):
                                    if l2[uu][vv]==x1.lower():
                                        ll[u][v][uu][vv]=p
            
            ch=check_1(l[ix])

            if ch==True:
                for u in range(3):
                    for v in range(3):
                        if ll1[u][v]==ll2[ix]:
                            ttt[u][v]=p
            
            grid()
            
            CH=check_1(ttt)
            if CH==True:
                os.system('cls')
                print()
                print(ttt[0][0]," | ",ttt[0][1]," | ",ttt[0][2])
                print("---+-----+---")
                print(ttt[1][0]," | ",ttt[1][1]," | ",ttt[1][2])
                print("---+-----+---")
                print(ttt[2][0]," | ",ttt[2][1]," | ",ttt[2][2])
                print()
                print("YOU WON!!!")
                break
            else:
                iii=0
                for ij in ttt:
                    for ji in ij:
                        if ji==' ':
                            iii=1
                if iii==0:
                    os.system('cls')
                    print()
                    print(ttt[0][0]," | ",ttt[0][1]," | ",ttt[0][2])
                    print("---+-----+---")
                    print(ttt[1][0]," | ",ttt[1][1]," | ",ttt[1][2])
                    print("---+-----+---")
                    print(ttt[2][0]," | ",ttt[2][1]," | ",ttt[2][2])
                    print()
                    print("TIE!!!")
                    break

            sleep(3)

            print("MY TURN")

            if n==0:
                i=l1.index(x1)
                n=1
            
            jj=0
            for t1 in range(3):
                for t2 in range(3):
                    if l2[t1][t2]==x1:
                        if ttt[t1][t2]==' ':
                            jj=1

            if jj==1:
                for d in l[i]:
                    if ' ' in d:
                        b=0
                        for d in l[i]:
                            for dd in d:
                                if dd==' ':
                                    while True:
                                        y,z=check_3(l[i])
                                        if y==None and z==None:
                                            y1,z1=check_2(l[i])
                                            if y1==None and z1==None:
                                                j=random.randint(0,2)
                                                k=random.randint(0,2)
                                            else:
                                                j,k=y1,z1
                                        else:
                                            j,k=y,z
                                        x=l2[j][k]

                                        if l[i][j][k]==' ':
                                            l[i][j][k]=c
                                            b=1
                                            break
                                if b==1:
                                    break
                            if b==1:
                                break
                    if b==1:
                        break
            else:
                while True:
                    i=random.randint(0,8)
                    j=random.randint(0,2)
                    k=random.randint(0,2)
                    
                    x=l2[j][k]
                    if l[i][j][k]==' ' and ttt[k][j]==' ':
                        l[i][j][k]=c
                        break
            
            ch=check_1(l[i])

            if ch==True:
                for u in range(3):
                    for v in range(3):
                        if ll1[u][v]==ll2[i]:
                            ttt[u][v]=c

            grid()
            print(f"I have put {c} at {x} of {ll2[i]}")

            CH=check_1(ttt)
            if CH==True:
                os.system('cls')
                print()
                print(ttt[0][0]," | ",ttt[0][1]," | ",ttt[0][2])
                print("---+-----+---")
                print(ttt[1][0]," | ",ttt[1][1]," | ",ttt[1][2])
                print("---+-----+---")
                print(ttt[2][0]," | ",ttt[2][1]," | ",ttt[2][2])
                print()
                print("I WON!!!")
                break
            else:
                iii=0
                for ij in ttt:
                    for ji in ij:
                        if ji==' ':
                            iii=1
                if iii==0:
                    os.system('cls')
                    print()
                    print(ttt[0][0]," | ",ttt[0][1]," | ",ttt[0][2])
                    print("---+-----+---")
                    print(ttt[1][0]," | ",ttt[1][1]," | ",ttt[1][2])
                    print("---+-----+---")
                    print(ttt[2][0]," | ",ttt[2][1]," | ",ttt[2][2])
                    print()
                    print("TIE!!!")
                    break

    elif s=='2':
        na=[n1,n2]

        print()
        grid()
        
        print(f"{na[0].upper()}'S TURN")

        while True:
            x=input(f"Where do you want to put x?")
            if x.lower() in l1:
                break
            else:
                print("Invaild Input!!")
        
        v1=-1
        while True:
            v1+=1
            if v1>1:
                v1=0

            print(f"{na[v1].upper()}'S TURN")

            i=l1.index(x.lower())

            jj=0
            for t1 in range(3):
                for t2 in range(3):
                    if l2[t1][t2]==x:
                        if ttt[t1][t2]==' ':
                            jj=1

            if jj==1:
                while True:
                    r=0
                    x1=input(f"Where do you want to put {'xo'[v1]} in {x.upper()}?")
                    x=x1
                    if x1 not in l1:
                        print("Invaild Input!")
                        continue

                    for k in range(3):
                        for q in range(3):
                            if l2[k][q]==x1:
                                if l[i][k][q]==' ':
                                    l[i][k][q]='xo'[v1]
                                    r=1
                                else:
                                    print("Invaild Input!")
                    
                    if r==1:
                        break
            else:
                while True:
                    x=input(f"Where do you want to put {'xo'[v1]}?").lower()
                    x1=x.upper()
                    if x1 in ll2:
                        while True:
                            x=input(f"Where do you want to put {'xo'[v1]}?")
                            if x.lower() in l1:
                                break
                            else:
                                print("Invaild Input!!")
                        break
                    else:
                        print("Invaild Input!!")
                
                for u in range(3):
                    for v in range(3):
                        if ll1[u][v]==x1:
                            for uu in range(3):
                                for vv in range(3):
                                    if l2[uu][vv]==x.lower():
                                        ll[u][v][uu][vv]='xo'[v1]
            
            ch=check_1(l[i])

            if ch==True:
                for u in range(3):
                    for v in range(3):
                        if ll1[u][v]==ll2[i]:
                            if ttt[u][v]==' ':
                                ttt[u][v]='xo'[v1]
            
            grid()
            
            CH=check_1(ttt)
            if CH==True:
                os.system('cls')
                print()
                print(ttt[0][0]," | ",ttt[0][1]," | ",ttt[0][2])
                print("---+-----+---")
                print(ttt[1][0]," | ",ttt[1][1]," | ",ttt[1][2])
                print("---+-----+---")
                print(ttt[2][0]," | ",ttt[2][1]," | ",ttt[2][2])
                print()
                print(f"{na[v1].upper()} WON!!!")
                break
            else:
                iii=0
                for ij in ttt:
                    for ji in ij:
                        if ji==' ':
                            iii=1
                if iii==0:
                    os.system('cls')
                    print()
                    print(ttt[0][0]," | ",ttt[0][1]," | ",ttt[0][2])
                    print("---+-----+---")
                    print(ttt[1][0]," | ",ttt[1][1]," | ",ttt[1][2])
                    print("---+-----+---")
                    print(ttt[2][0]," | ",ttt[2][1]," | ",ttt[2][2])
                    print()
                    print("TIE!!!")
                    break

def dropdead():
    os.system('cls')
    print("Let's play drop dead!!")
    print("Rules of the game are simple. The players will roll five dices if any of the dice does not roll 2 or 5 then the player can add those number to her/his score. If the person rolls even one 2 or one 5 then she/he will need to remove that dice and she/he can not add any any number to there score.")

    while True:
        n=int(input("\nEnter number of players playing:"))
        if n>0:
            break
        else:
            print("Atleast one player is required!")

    p=[]
    cc=[]

    for i in range(n):
        if i==0:
            x=input("Enter name of the 1st player:")
        elif i==1:
            x=input("Enter name of the 2nd player:")
        elif i==2:
            x=input("Enter name of the 3rd player:")
        else:
            x=input(f"Enter name of the {i+1}th player:")
        p.append(x)

    while True:
        n1=int(input("Enter number of computer generated opponents you want:"))
        if n==1:
            if n1<1:
                print("You need atleast one computer generated opponent!")
                continue
            else:
                break
        else:
            if n1<0:
                print("Invaild Input!!")
            else:
                break

    for i in range(n1):
        p.append(f'C{i+1}')
        cc.append(f'C{i+1}')

    print("\nLet's decide who will go first!")

    dd={}
    l=[]
    for i in p:
        s=0
        print(f"\n{i.upper()}'S TURN")
        print()
        
        if i not in cc:
            print("Roll the dices!")
            print("Press r")
            while True:
                if msvcrt.kbhit():
                    w=msvcrt.getch()
                    q=str(w)
                    k=q[-2]
                    if k=='r':
                        a=random.randint(1,6)
                        b=random.randint(1,6)
                        c=random.randint(1,6)
                        d=random.randint(1,6)
                        e=random.randint(1,6)
                        break
                    else:
                        print("PRESS r!!!")
        else:
            print("Rolling the dices...")
            sleep(2)
            a=random.randint(1,6)
            b=random.randint(1,6)
            c=random.randint(1,6)
            d=random.randint(1,6)
            e=random.randint(1,6)
        
        s=a+b+c+d+e
        print("Dice rolled:",(a,b,c,d,e))
        print("Total:",s)
        dd[i]=s
        l.append(s)

        sleep(5)

    l.sort(reverse=True)

    ps={}
    l1=[]

    for u in l:
        for v in dd.keys():
            if dd[v]==u:
                ps[v]=u
                l1.append(v)

    print(f"\nTherefore {l1[0]} will start!")
    sleep(3)

    os.system('cls')
    for i in ps.keys():
        print()
        print(f"{i}'s Turn")
        
        ctr=0
        n=5

        while True:
            d1=[]
            
            if i in cc:
                print("\nRolling the dices...")
                sleep(2)
            else:
                print("\nPress r")
                while True:
                    if msvcrt.kbhit():
                        w=msvcrt.getch()
                        p=str(w)
                        k=p[-2]
                        if k=='r':
                            break
                        else:
                            print("PRESS r!!!")
            
            for j in range(n):
                dice=random.randint(1,6)
                d1.append(dice)

            print(f"Dices rolled:",d1)

            if (2 in d1 or 5 in d1):
                n1=0
                for k in d1:
                    if k in (2,5):
                        n-=1
                        n1+=1
                if n1>1:
                    print(n1,"dices are dead!!")
                elif n1==1:
                    print("1 dice is dead!!")
            else:
                for k in d1:
                    ctr+=k
            
            print(f"{i}'s Score:",ctr)
            sleep(2)

            if n==0:
                break
        
        ps[i]=ctr

    print()
    for i in ps.keys():
        print(i,':',ps[i])

    print()
    v=[]
    for i in ps.values():
        v.append(i)
    v.sort(reverse=True)
    n=[]

    for k in range(len(v)):
        for i in ps.keys():
            if ps[i]==v[k]:
                if i not in n:
                    n.append(i)
                    break

    for i in range(len(n)):
        if i==0:
            print(n[i],f"is {i+1}st")
        elif i==1:
            print(n[i],f"is {i+1}nd")
        elif i==2:
            print(n[i],f"is {i+1}rd")
        else:
            print(n[i],f"is {i+1}th")

def gulam_chor():

    os.system('clear')
    print("Let's play gadha-chor!!!")

    name=input("Enter your name:")

    pl={}
    pl1={}

    pl1[name]=[]

    p=[]
    c=[]
    l=[]

    p.append(name)

    while True:
        n1=int(input("Enter number of computer generated opponents you want:"))
        if n1<1:
            print("You need atleast one computer generated opponent!")
            continue
        else:
            break

    for i in range(n1):
        pl1[f'C{i+1}']=[]
        p.append(f'C{i+1}')
        c.append(f'C{i+1}')

    cards=['A','A','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10','J','J','K','K','Q','Q','Joker']
    random.shuffle(cards)

    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    k=0
    while True:
        for i in range(len(p)):
            pl1[p[i]].append(cards[0])
            cards.pop(0)
            if cards==[]:
                k=1
                break
        if k==1:
            break

    print("Your cards:",pl1[name])

    for i in pl1.keys():
        ll=[]
        for j in pl1[i]:
            if pl1[i].count(j)%2!=0:
                if j not in ll:
                    ll.append(j)
        pl[i]=ll

    if len(pl[name])<len(pl1[name]):
        print("The duplicate cards are removed!!!")

    print("Your cards:",pl[name])

    del pl1

    s=[]
    w=[]
    e=0
    q=0
    while True:
        q+=1
        if len(pl)==0:
            break

        i=0
        while i<len(p):
            if p[i] in w:
                continue
            
            if q==1: 
                sleep(5)
            else:
                sleep(0.5)
            os.system('clear')
            
            print(f"{p[i].upper()}'S TURN")

            if p[i]==name:
                try:
                    for j in pl[p[i+1]]:
                        print(" -----",end='     ')
                    print()
                    for j in pl[p[i+1]]:
                        print("|  M  |",end='    ')
                    print()
                    for j in pl[p[i+1]]:
                        print("|  A  |",end='    ')
                    print()
                    for j in pl[p[i+1]]:
                        print(" -----",end='     ')
                    print()
                    print('   ',end='')
                    for j in range(len(pl[p[i+1]])):
                        print(alpha[j],end='          ')
                        l.append(alpha[j])
                except:
                    for j in pl[p[0]]:
                        print(" -----",end='     ')
                    print()
                    for j in pl[p[0]]:
                        print("|  M  |",end='    ')
                    print()
                    for j in pl[p[0]]:
                        print("|  A  |",end='    ')
                    print()
                    for j in pl[p[0]]:
                        print(" -----",end='     ')
                    print()
                    print('   ',end='')
                    for j in range(len(pl[p[0]])):
                        print(alpha[j],end='          ')
                        l.append(alpha[j])

                while True:
                    x=input("\nEnter the chosen card>").upper()
                    if x in l or len(pl[p[i]])<=1:
                        break
                    else:
                        print("Invalid Input!",end='')
                    
                try:
                    x1=random.choice(pl[p[i+1]])
                    pl[p[i+1]].remove(x1)
                except:
                    x1=random.choice(pl[p[0]])
                    pl[p[0]].remove(x1)
                
                print("The card is",x1)
                pl[p[i]].append(x1)
                
                sleep(0.5)
                
                print("Your cards:",pl[p[i]])
                n=len(pl[p[i]])
                
                pp=[]
                for j in pl[p[i]]:
                    if pl[p[i]].count(j)>1:
                        if pl[p[i]].count(j)%2==0:
                            pass
                        else:
                            if j not in pp:
                                pp.append(j)
                    else:
                        pp.append(j)
                
                pl[p[i]]=pp
                
                sleep(2)
                
                if len(pp)<n:
                    print("Your cards:",pp)
                    print("The duplicate cards are removed!!!")
                
                for k in range(len(p)):
                    try:
                        if pl[p[k]]==[]:
                            os.system('clear')
                            w.append(p[k])
                            if len(w)==1:
                                u='1st'
                            elif len(w)==2:
                                u='2nd'
                            elif len(w)==3:
                                u='3rd'
                            else:
                                u=str(len(w))+'th'

                            print(p[k].upper(),f"came {u}!!")
                            s.append(f"{str(p[k].upper())} came {u}!!")
                            pl.pop(p[k])
                            p.pop(k)
                            i-=1

                    except:
                        continue
                
                if len(p)==0:
                    e=1

            else:

                try:
                    x1=random.choice(pl[p[i+1]])
                    pl[p[i+1]].remove(x1)
                except:
                    x1=random.choice(pl[p[0]])
                    pl[p[0]].remove(x1)
                pl[p[i]].append(x1)
                n=len(pl[p[i]])
                
                sleep(0.5)

                pp=[]
                for j in pl[p[i]]:
                    if pl[p[i]].count(j)>1:
                        if pl[p[i]].count(j)%2==0:
                            pass
                        else:
                            if j not in pp:
                                pp.append(j)
                    else:
                        pp.append(j)
                
                pl[p[i]]=pp
                
                print("Card picked!")
                sleep(0.5)
                
                if len(pp)<n:
                    print("The duplicate cards are removed!!!")
                
                for k in range(len(p)):
                    try:
                        if pl[p[k]]==[]:
                            os.system('clear')
                            w.append(p[k])
                            if len(w)==1:
                                u='1st'
                            elif len(w)==2:
                                u='2nd'
                            elif len(w)==3:
                                u='3rd'
                            else:
                                u=str(len(w))+'th'

                            print(p[k].upper(),f"came {u}!!")
                            s.append(f"{str(p[k].upper())} came {u}!!")
                            pl.pop(p[k])
                            p.pop(k)
                            i-=1
                    except:
                        continue
                
                if len(p)==1:
                    e=1
            
            i+=1

        if e==1:
            s.append(f"{str(p[0])} came last!!")
            
            os.system('clear')
            for i in s:
                print(i)

            break

def memory():
    s={'∆':2,'¢':2,'%':2,'@':2,'#':2,'&':2,'£':2,'X':2}
    s1=['∆','¢','%','@','#','&','£','X']
    l=[]
    l1=[]

    alpha='abcd'
    z=0
    while True:
        z+=1
        if z==1:
            n=-1
            print("     ",end='')
            for i in range(4):
                print(i+1,end='     ')
            print()
            for i in range(4):
                l3=[]
                n+=1
                print('  +',end='')
                print('-----+'*4)
                print(f'{alpha[i]} |',end='')
                for j in range(4):
                    while True:
                        x=random.choice(s1)
                        if s[x]!=0:
                            break
                    print(f'  {x}  |',end='')
                    l3.append(x)
                    s[x]-=1
                print()
                l.append(l3)
            print('  +',end='')
            print('-----+'*4)

            sleep(5)
        os.system('cls')

        print("     ",end='')
        for i in range(4):
            print(i+1,end='     ')
        print()
        for i in range(4):
            print('  +',end='')
            print('-----+'*4)
            print(f'{alpha[i]} |',end='')
            for j in range(4):
                if l[i][j] in l1:
                    print(f'  {l[i][j]}  |',end='')
                else:    
                    print(f' MA  |',end='')
            print()
        print('  +',end='')
        print('-----+'*4)
        
        while True:
            x=input("Enter the coordinates of the 1st card:")
            if x[0] not in 'abcd' or x[1] not in '1234':
                print("Invaild Input!")
            else:
                break
        

        print("     ",end='')
        for i in range(4):
            print(i+1,end='     ')
        print()
        for i in range(4):
            print('  +',end='')
            print('-----+'*4)
            print(f'{alpha[i]} |',end='')
            for j in range(4):
                if i==alpha.index(x[0]) and j==int(x[1])-1 or l[i][j] in l1:
                    print(f'  {l[i][j]}  |',end='')
                else:    
                    print(f' MA  |',end='')
            print()
        print('  +',end='')
        print('-----+'*4)

        while True:
            x1=input("Enter the coordinates of the 2st card:")
            if x1[0] not in 'abcd' or x1[1] not in '1234':
                print("Invaild Input!")
            else:
                break

        print("     ",end='')
        for i in range(4):
            print(i+1,end='     ')
        print()
        for i in range(4):
            print('  +',end='')
            print('-----+'*4)
            print(f'{alpha[i]} |',end='')
            for j in range(4):
                if i==alpha.index(x[0]) and j==int(x[1])-1 or l[i][j] in l1:
                    print(f'  {l[i][j]}  |',end='')
                elif i==alpha.index(x1[0]) and j==int(x1[1])-1 or l[i][j] in l1:
                    print(f'  {l[i][j]}  |',end='')
                else:    
                    print(f' MA  |',end='')
            print()
        print('  +',end='')
        print('-----+'*4)

        sleep(3)
        
        a1=alpha.index(x[0])
        b1=int(x[1])-1
        a2=alpha.index(x1[0])
        b2=int(x1[1])-1

        if l[a1][b1]==l[a2][b2]:
            if (l[a1][b1] and l[a2][b2]) not in l1: 
                l1.append(l[a1][b1])
                l1.append(l[a2][b2])

            if len(l1)==16:
                print("You have completed the puzzle!!")
                break

            print("     ",end='')
            for i in range(4):
                print(i+1,end='     ')
            print()
            for i in range(4):
                print('  +',end='')
                print('-----+'*4)
                print(f'{alpha[i]} |',end='')
                for j in range(4):
                    if i==a1 and j==b1 or l[i][j] in l1:
                        print(f'  {l[i][j]}  |',end='')
                    elif i==a2 and j==b2 or l[i][j] in l1:
                        print(f'  {l[i][j]}  |',end='')
                    else:    
                        print(f' MA  |',end='')
                print()
            print('  +',end='')
            print('-----+'*4)

        else:
            print("     ",end='')
            for i in range(4):
                print(i+1,end='     ')
            print()
            for i in range(4):
                print('  +',end='')
                print('-----+'*4)
                print(f'{alpha[i]} |',end='')
                for j in range(4):
                    print(f' MA  |',end='')
                print()
            print('  +',end='')
            print('-----+'*4)

def mastermind():
    print("I will think of a 4 digit number and you have to guess it!!")

    while True:
        n=random.randint(1000,9999)

        s=str(n)

        k=0
        for i in range(len(s)):
            for j in range(i):
                if s[i]==s[j]:
                    k=1

        if k==1:
            continue
        else:
            break

    l=[]
    ch=0
    while True:
        while True:
            n1=input("Enter a 4 digit number:")
            if len(n1)==4:
                if n1 in l:
                    print("You have already entered this number!!")
                    continue
                else:
                    l.append(n1)
                break
            else:
                print("Enter a 4 digit number!")
        ch+=1

        if n1==s:
            print("You guessed the number!!!")
            print(f"You took {ch} chances!!")
            break
        else:
            c1=0
            c2=0
            for i in n1:
                for j in s:
                    if i==j:
                        c1+=1
                        if n1.index(i)==s.index(j):
                            c2+=1
            
            print(f"{c1} numbers are correct and {c2} are in the correct position!")

def snl():
    player=1
    ai=1
    ladder={4:14,9:31,20:38,28:84,40:59,51:67,63:81,71:91}
    snake={17:7,54:34,62:19,64:60,87:24,93:73,95:75,99:78}

    i=0

    while player<=100 and ai<=100:    
        if i%2==0:
            print("PLAYER'S TURN")
            x=''
            print("Press r to roll the dice!!")
            while True:
                if msvcrt.kbhit():
                    w=msvcrt.getch()
                    p=str(w)
                    k=p[-2]
                    if k=='r':
                        break
                    else:
                        print("Press r!!!")
            
            print("Rolling the dice...")
            sleep(2)
            dice=random.randint(1,6)

            if dice==6:
                i+=0
            else:
                i+=1
            print("Dice:",dice)
            player+=dice
            if player>100:
                player-=dice
                i+=0
                print("Player:",player)
                continue
            print("Player:",player)
            if player in ladder.keys():
                player=ladder[player]
                print("Player has took a ladder and reached",player)
            elif player in snake.keys():
                player=snake[player]
                print("Player has been bitten by a snake and reached",player)
            elif player==100:
                print('PLAYER WIN!')
                break
        else:
            print("AI'S TURN")
            print("Rolling the dice...")
            sleep(2)
            dice=random.randint(1,6)
            if dice==6:
                i+=0
            else:
                i+=1
            print("Dice:",dice)
            ai+=dice
            if ai>100:
                ai-=dice
                i+=0
                print("AI:",ai)
                continue
            print("AI:",ai)
            if ai in ladder.keys():
                ai=ladder[ai]
                print("AI has took a ladder and reached",ai)
            elif ai in snake.keys():
                ai=snake[ai]
                print("AI has been bitten by a snake and reached",ai)
            elif ai==100:
                print('AI WIN!')
                break

def paswdgen():
    d={'q':'a','a':'z','z':'q','w':'s','s':'x','x':'w','e':'d','d':'c','c':'e','r':'f','f':'v','v':'r','t':'g','g':'b','b':'t','y':'h','h':'n','n':'y','u':'j','j':'m','m':'u','i':'k','k':'i','o':'l','l':'o','p':'p'}
    D={'Q':'A','A':'Z','Z':'Q','W':'S','S':'X','X':'W','E':'D','D':'C','C':'E','R':'F','F':'V','V':'R','T':'G','G':'B','B':'T','Y':'H','H':'N','N':'Y','U':'J','J':'M','M':'U','I':'K','K':'I','O':'L','L':'O','P':'P'}
    n={'1':')','2':'(','3':'*','4':'&','5':'^','6':'%','7':'$','8':'#','9':'@','0':'!'}
    while True:
        print("You can write 'exit' if you don't want to encrypt or decrypt.")
        z=input("Do you want to encrypt or decrypt?")
        if z.lower()=="e":
            x = input("Enter something to be encrypted: ")
            y=''
            for i in x:
                if i.isupper():
                    y+=D[i]
                elif i.islower():
                    y+=d[i]
                elif i==' ':
                    y+='-'
                elif i.isnumeric():
                    y+=n[i]
                else:
                    if i in n.values():
                        for k in n.keys():
                            if n[k]==i:
                                y+=str(k)
                    elif i==',':
                        y+='.'
                    elif i=='.':
                        y+=','
                    elif i=='?':
                        y+='|'
                    else:
                        y+=i
            print(y)
            l=list(y)
            print(l)
            random.shuffle(l)
            y1= ''.join(l)
            print(y1)
            continue
        elif z.lower()=='d':
            c=input("Enter something to be decrypted: ")
            if c==y1:
                a=y
            b=''
            for i in a:
                if i.isupper():
                    for j in D.keys():
                        if i==D[j]:
                            b+=j
                elif i.islower():
                    for j in d.keys():
                        if i==d[j]:
                            b+=j
                elif i=='-':
                    b+=' '
                elif i in n.values():
                    for k in n.keys():
                        if n[k]==i:
                            b+=str(k)
                elif i.isnumeric():
                    b+=n[i]
                elif i=='.':
                    b+=','
                elif i==',':
                    b+='.'
                elif i=='|':
                    b+='?'
                else:
                    b+=i
            print(b)
            continue

        elif z.lower()=='exit':
            break   
        else:
            print("Invalid input!")
            continue

def sos():
    while True:
        row=int(input("Enter number of rows:"))
        col=int(input("Enter number of coloums:"))
        if (row and col)<3:
            print("Invaild Input!")
            continue
        else:
            break

    while True:
        p1=input("Choose s or o>")
        p=p1.upper()

        if p in ('S','O'):
            if p.lower()=='s':
                c='O'
            else:
                c='S'
            break
        else:
            print("Invalid Input!")
            continue

    l=[]
    la=[]
    ln=[]

    alpha='abcdefghijklmnopqrstuvwxyz'

    for i in range(row):
        l1=[]
        for j in range(col):
            l1.append(' ')
        l.append(l1)

    print('    ',end='')
    for i in range(col):
        print(i+1,end='   ')
        ln.append(str(i+1))
    print()
    for i in range(row):
        print('  +',end='')
        print('---+'*col)
        print(f'{alpha[i]} |',end='')
        la.append(alpha[i])
        for j in range(col):
            print(f' {l[i][j]} |',end='')
        print()
    print('  +',end='')
    print('---+'*col)

    def check():
        n=0
        for i in range(row):
            for j in range(col):
                if l[i][j]=='S':
                    try:
                        if l[i][j+1]=='O':
                            if l[i][j+2]=='S':
                                n+=1
                        elif l[i+1][j]=='O':
                            if l[i+2][j]=='S':
                                n+=1
                    except:
                        pass
        return n

    def check_1():
        for i in range(row):
            for j in range(col):
                if l[i][j]=='S':
                    try:
                        if l[i][j+1]=='O':
                            try:
                                if l[i][j+2]==' ':
                                    return i,j+2
                            except:
                                return ''
                        elif l[i+1][j]=='O':
                            try:
                                if l[i+2][j]==' ':
                                    return i+2,j
                            except:
                                return ''
                        elif l[i][j+2]=='S':
                            try:
                                if l[i][j+1]==' ':
                                    return i,j+1
                            except:
                                return ''
                        elif l[i+2][j]=='S':
                            try:
                                if l[i+1][j]==' ':
                                    return i+1,j
                            except:
                                return ''
                        elif l[i][j-1]=='O':
                            try:
                                if l[i][j-2]==' ':
                                    return i,j-2
                            except:
                                return ''
                        elif l[i-1][j]=='O':
                            try:
                                if l[i-2][j]==' ':
                                    return i-2,j
                            except:
                                return ''
                        elif l[i][j-2]=='S':
                            try:
                                if l[i][j-1]==' ':
                                    return i,j-1
                            except:
                                return ''
                        elif l[i-2][j]=='S':
                            try:
                                if l[i-1][j]==' ':
                                    return i-1,j
                            except:
                                return ''
                    except:
                        return ''

    pscore=0
    cscore=0

    n0=0

    w=0
    while w==0:
        w=1
        
        print("YOUR TURN")
        
        while True:
            x=input(f"Where do you want to put {p}?")
            
            if x[0] in la and x[1] in ln:
                i=la.index(x[0])
                j=ln.index(x[1])
                
                if l[i][j]==' ':
                    l[i][j]=p
                    break
                else:
                    print("Invalid Move!!")
            else:
                print("Invaild Position!!")
                continue
        
        os.system('cls')
        print('    ',end='')
        for i in range(col):
            print(i+1,end='   ')
            ln.append(str(i+1))
        print()
        for i in range(row):
            print('  +',end='')
            print('---+'*col)
            print(f'{alpha[i]} |',end='')
            la.append(alpha[i])
            for j in range(col):
                print(f' {l[i][j]} |',end='')
            print()
        print('  +',end='')
        print('---+'*col)
        
        #print('check:',check(),'cscore:',cscore,'n0:',n0)
        n1=check()
        pscore+=n1-n0
        if cscore<0:
            cscore=0
        n0=n1
        #print('check:',check(),'cscore:',cscore,'n0:',n0)
        
        for i in range(row):
            for j in range(col):
                if l[i][j]==' ':
                    w=0
        
        print('p:',pscore,'c:',cscore)
        if w==1:
            if pscore>cscore:
                print("YOU WON!!!")
            elif cscore>pscore:
                print("I WON!!!")
            else:
                print("TIE!!!")
            break

        print("MY TURN")

        w=0
        c1=check_1()
        if c1 in ('',None):
            while True:
                x=random.randrange(0,row)
                y=random.randrange(0,col)
                if l[x][y]!=' ':
                    continue
                else:
                    l[x][y]=c
                    break
        else:
            l[c1[0]][c1[1]]=c
        
        os.system('cls')
        print('    ',end='')
        for i in range(col):
            print(i+1,end='   ')
            ln.append(str(i+1))
        print()
        for i in range(row):
            print('  +',end='')
            print('---+'*col)
            print(f'{alpha[i]} |',end='')
            la.append(alpha[i])
            for j in range(col):
                print(f' {l[i][j]} |',end='')
            print()
        print('  +',end='')
        print('---+'*col)
        
        #print('check:',check(),'cscore:',cscore,'n0:',n0)
        n1=check()
        cscore+=n1-n0
        if cscore<0:
            cscore=0
        n0=n1
        #print('check:',check(),'cscore:',cscore,'n0:',n0)

        for i in range(row):
            for j in range(col):
                if l[i][j]==' ':
                    w=0
        
        print('p:',pscore,'c:',cscore)
        if w==1:
            if pscore>cscore:
                print("YOU WON!!!")
            elif cscore>pscore:
                print("I WON!!!")
            else:
                print("TIE!!!")

def rps():
    print("Let's play Rock, Paper and Scissors. Can you beat me!?")
    print("For your convenience you can write r for rock, p for paper and s for scissors :)")
    print("And don't worry I will count our scores.")

    CSetScore=0
    PSetScore=0

    rps=['r','p','s']
    d={'r':0, 'p':0, 's':0}

    z=int(input("You want to play best of "))
    z1=z//4

    i=1
    while i<=z:
        CScore=0
        PScore=0
        while True:
            x1=input("What's your move? ")
            x=x1.lower()
            if x not in rps:
                print("Invalid input")
                continue
            else:
                break

        if i in range(1,z1):
            d[x]+=1
            y=random.choice(rps)
        else:
            if i%2==0:
                k=max(d.values())
                for j in d.keys():
                    if d[str(j)]==k:
                        if str(j)=='r':
                            y='p'
                        elif str(j)=='p':
                            y='s'
                        elif str(j)=='s':
                            y='r'
            else:
                y=random.choice(rps)
        
        print("My move is",y)
        if x=='r':
            if y=='r':
                print(":|")
            elif y=='p':
                print(":)")
                CScore+=1
            elif y=='s':
                print(":(")
                PScore+=1
        elif x=='p':
            if y=='r':
                print(":(")
                PScore+=1
            elif y=='p':
                print(":|")
            elif y=='s':
                print(":)")
                CScore+=1
        elif x=='s':
            if y=='r':
                print(":)")
                CScore+=1
            elif y=='p':
                print(":(")
                PScore+=1
            elif y=='s':
                print(":|")
        
        if CScore>PScore:
            CSetScore+=1
        elif PScore>CScore:
            PSetScore+=1
            
        i+=1

    print("My score is",CSetScore,".")
    print("Your score is",PSetScore,".")

    if z-(CSetScore+PSetScore)>1:
        print(z-(CSetScore+PSetScore),"were draw.")
    elif z-(CSetScore+PSetScore)==1:
        print(z-(CSetScore+PSetScore),"was draw.")

    if CSetScore>PSetScore:
        print("I WON!! Better luck next time.")
    elif PSetScore>CSetScore:
        print("Congrats!! YOU WON!!")
    else:
        print("DRAW!!!")

def oddeven():
    print("Let's play cricket without bat and ball!!!")
    print("Yeah! You guessed it we are playing odd even.")
    print("Don't worry I count our scores.")

    while True:
        player1=input("So what do you choose odd or even? ")
        player=player1.lower()
        comp=''
        if player=='odd':
            print("Good then I have even!")
            comp='even'
            break
        elif player=='even':
            print("Good then I have odd!")
            comp='odd'
            break
        else:
            print("Please type what is asked, don't be oversmart! Sorry if I'm rude.")
            continue

    numbers=[1,2,3,4,5,6,7,8,9,10]
    print("Let's decide who will bat first and ball first.")
    while True:
        x=int(input("Your move:"))
        if x in numbers:
            break
        else:
            print("Invalid input")
            continue
    y=random.randint(1,10)
    print("My move is",y)
    Player=''
    Comp=''
    if (x+y)%2==0:
        if player=='odd':
            print("It's even that means I win :)")
            z=random.choice(["Bat","Ball"])
            print(f"Therefore I choose to {z} first")
            Comp=z
            for i in ("Bat","Ball"):
                if i!=z:
                    print(f"That means you have {i}")
                    Player=i
        else:
            print("It's even that means you win :(")
            while True:
                z1=input("What do you choose? ")
                if z1 in ('bat','ball','Bat','Ball'):
                    if z1[0]=='b':
                        z2=z1.replace('b','B')
                    else:
                        z2=z1
                    break
                else:
                    print("Invalid input")
                    continue
            Player=z2
            for i in (["Bat","Ball"]):
                if i!=z2:
                    print(f"That means I have {i}")
                    Comp=i
    else:
        if player=='even':
            print("It's odd that means I win :)")
            z=random.choice(["Bat","Ball"])
            print(f"Therefore I choose to {z} first")
            Comp=z
            for i in ("Bat","Ball"):
                if i!=z:
                    print(f"That means you have {i}")
                    Player=i
        else:
            print("It's odd that means you win :(")
            while True:
                z1=input("What do you choose? ")
                if z1 in ('bat','ball','Bat','Ball'):
                    if z1[0]=='b':
                        z2=z1.replace('b','B')
                    else:
                        z2=z1
                    break
                else:
                    print("Invalid input")
                    continue
            Player=z2
            for i in ("Bat","Ball"):
                if i!=z2:
                    print(f"That means I have {i}")
                    Comp=i

    print("Let's start!")

    if Player=="Bat" and Comp=="Ball":
        PlayerScore=0
        CompScore=0
        
        d={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
        l=[]
        count=0

        while True:    
            while True:
                while True:
                    x=int(input("Your move:"))
                    if x not in numbers:
                        print("Invalid input")
                        continue
                    else:
                        break
                if x in numbers:
                    l.append(str(x))
                    d[str(x)]+=1
                    count+=1
                    if count>10:
                        for i in d.keys():
                            d[str(l[count-11])]-=1
                    break
                else:
                    print("Invalid input")
                    continue
            if count>10:
                if count%2==0:
                    m=max(d.values())
                    for i in d.keys():
                        if d[i]==m:
                            y=int(i)
                else:
                    y=random.randint(1,10)
            else:
                y=random.randint(1,10)
            print("My move:",y)
            if x==y:
                print("Out!!")
                print("Your score is",PlayerScore,".")
                print("My turn to bat and I need",PlayerScore+1,"runs to win.")
                break
            else:
                PlayerScore+=x
        
        d={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
        l=[]
        count=0
        
        while True:
            while True:
                while True:
                    x=int(input("Your move:"))
                    if x not in numbers:
                        print("Invalid input")
                        continue
                    else:
                        break
                if x in numbers:
                    l.append(str(x))
                    d[str(x)]+=1
                    count+=1
                    if count>10:
                        for i in d.keys():
                            d[str(l[count-11])]-=1
                    break
                else:
                    print("Invalid input")
                    continue
            if count>10:
                if count%2==0:
                    m=min(d.values())
                    for i in d.keys():
                        if d[i]==m:
                            y=int(i)
                else:
                    y=random.randint(1,10)
            else:
                y=random.randint(1,10)
            print("My move:",y)
            if x==y:
                print("Out!!")
                break
            else:
                CompScore+=y
                if CompScore>PlayerScore:
                    print("My score is",CompScore)
                    print("I WON!! Better luck next time :)")
                    break

        if CompScore==PlayerScore:
            print("My score is",CompScore)
            print("The match tied!!!")
        elif CompScore<PlayerScore:
            print("My score is",CompScore)
            print("Congrats!!You WON!!")

    else:
        PlayerScore=0
        CompScore=0

        d={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
        l=[]
        count=0

        while True:    
            while True:
                while True:
                    x=int(input("Your move:"))
                    if x not in numbers:
                        print("Invalid input")
                        continue
                    else:
                        break
                if x in numbers:
                    l.append(str(x))
                    d[str(x)]+=1
                    count+=1
                    if count>10:
                        for i in d.keys():
                            d[str(l[count-11])]-=1
                    break
                else:
                    print("Invalid input")
                    continue
            if count>10:
                if count%2==0:
                    m=min(d.values())
                    for i in d.keys():
                        if d[i]==m:
                            y=int(i)
                else:
                    y=random.randint(1,10)
            else:
                y=random.randint(1,10)
            print("My move:",y)
            if x==y:
                print("Out!!")
                print("My score is",CompScore,".")
                print("Your turn to bat and you need",CompScore+1,"runs to win.")
                break
            else:
                CompScore+=y
        
        d={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
        l=[]
        count=0

        while True:
            while True:
                while True:
                    x=int(input("Your move:"))
                    if x not in numbers:
                        print("Invalid input")
                        continue
                    else:
                        break
                if x in numbers:
                    l.append(str(x))
                    d[str(x)]+=1
                    count+=1
                    if count>10:
                        for i in d.keys():
                            d[str(l[count-11])]-=1
                    break
                else:
                    print("Invalid input")
                    continue
            if count>10:
                if count%2==0:
                    m=max(d.values())
                    for i in d.keys():
                        if d[i]==m:
                            y=int(i)
                else:
                    y=random.randint(1,10)
            else:
                y=random.randint(1,10)
            print("My move:",y)
            if x==y:
                print("Out!!")
                break
            else:
                PlayerScore+=x
                if PlayerScore>CompScore:
                    print("Your score is",PlayerScore)
                    print("You WON!!")
                    break
                
        if CompScore==PlayerScore:
            print("Your score is",PlayerScore)
            print("The match tied!!!")
        elif CompScore>PlayerScore:
            print("Your score is",PlayerScore)
            print("I WON!! Better luck next time :)")

def numguesser():
    print("Guess the number, which is between 1 to 100!! And see who takes the least chances!! ")

    n=random.randint(1,100)
    c=0
    while True:
        x=int(input("Enter number:"))

        if x==n:
            print("You guessed the number!!!!")
            print(f"You took {c} chances!")
            break
        elif x>n:
            print("My number is lesser!!")
            c+=1
        elif x<n:
            print("My number is greater!!")
            c+=1

def owzthat():
    
    print("Let's play Owzthat!!!")

    while True:
        x=input("Choose Heads or Tails>")
        if x.lower()=='heads':
            print("So I have tails!")
            break
        elif x.lower()=='tails':
            print("So I have heads!")
            break
        else:
            print("Invaild Input!")
            continue

    print("Tossing the coin...")
    sleep(2)
    y=random.choice(['heads','tails'])
    print(f"Its {y}!!!")

    n=-1
    if y==x:
        print("You won!")
        s=input("What do you choose?")
        if s.lower()=='bat':
            print("So I have ball!")
            print("So you will roll the die!")
            n=0
        elif s.lower()=='ball':
            print("So I have bat!")
            print("So I will roll the die!")
            n=1
    else:
        print("I won!")
        s=random.choice(['bat','ball'])
        print(f"I choose {s}!")
        if s.lower()=='bat':
            print("So you have ball!")
            print("So I will roll the die!")
            n=1
        elif s.lower()=='ball':
            print("So you have bat!")
            print("So you will roll the die!")
            n=0

    def bdice():
        x=random.choice(['1','2','3','4','owzthat','6'])
        return x

    def udice():
        x=random.choice(['bowled','stumped','caught','not out','no ball','L.B.W.'])
        return x

    pruns=0
    cruns=0

    if n==0:
        x=''
        while True:
            print("Press r to roll!!")
            while True:
                if msvcrt.kbhit():
                    k=msvcrt.getch()
                    p=str(k)
                    j=p[-2]
                    if j=='r':
                        x='roll'
                        break
            
            if x=='roll':
                y=bdice()
                print("Dice rolled",y)
                if y!='owzthat':
                    pruns+=int(y)
                    print("Your runs:",pruns)
                else:
                    print("OWZTHAT!!!")
                    x1=udice()
                    print(f"Umpire's decision: {x1}")
                    if x1 in ('not out','no ball'):
                        continue
                    else:
                        print(f"You made {pruns}!!")
                        print(f"I need {pruns+1} runs to win.")
                        break

        while True:
            y=bdice()
            print("I rolled the die!")
            print("Dice rolled",y)
            sleep(3)

            if y!='owzthat':
                cruns+=int(y)
                print("My runs:",cruns)
                if cruns>pruns:
                    print("I WON!!!")
                    break
            else:
                print("OWZTHAT!!!")
                x1=udice()
                print(f"Umpire's decision: {x1}")
                if x1 in ('not out','no ball'):
                    continue
                else:
                    print(f"I made {cruns}!!")
                    if cruns<pruns:
                        print("YOU WON!!!")
                        break
                    elif cruns==pruns:
                        print("TIE!!!")
                        break

    else:
        x=''
        while True:
            y=bdice()
            print("I rolled the die!")
            print("Dice rolled",y)
            sleep(3)

            if y!='owzthat':
                cruns+=int(y)
                print("My runs:",cruns)
            else:
                print("OWZTHAT!!!")
                x1=udice()
                print(f"Umpire's decision: {x1}")
                if x1 in ('not out','no ball'):
                    continue
                else:
                    print(f"I made {cruns}!!")
                    print(f"You need {cruns+1} runs to win.")
                    break
        
        while True:
            print("Press r to roll!!")
            while True:
                if msvcrt.kbhit():
                    k=msvcrt.getch()
                    p=str(k)
                    j=p[-2]
                    if j=='r':
                        x='roll'
                        break 
            
            if x=='roll':
                y=bdice()
                print("Dice rolled",y)
                if y!='owzthat':
                    pruns+=int(y)
                    print("Your runs:",pruns)
                    if cruns<pruns:
                        print("YOU WON!!!")
                        break
                    elif cruns==pruns:
                        print("TIE!!!")
                        break
                else:
                    print("OWZTHAT!!!")
                    x1=udice()
                    print(f"Umpire's decision: {x1}")
                    if x1 in ('not out','no ball'):
                        continue
                    else:
                        print(f"You made {pruns}!!")
                        if cruns>pruns:
                            print("I WON!!!")
                            break
                        elif cruns==pruns:
                            print("TIE!!!")
                            break

guiwindow()