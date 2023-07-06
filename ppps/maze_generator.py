import random
from time import sleep
import os
cols = int(input("Enter no. of cols: "))
rows = cols
a,row_a,col_a,og,fun = '#',0,0,['up','down','left','right'],['up','down','left','right','top_right','top_left','bottom_right','bottom_left']
l = [[" " for i in range(cols)] for j in range(rows)]
l[row_a][col_a] = a
def grid():
    l[row_a][col_a] = a
    print("+"+"-"*cols*5+"+")
    for row in l:
        print('|'+str(row)+'|')
    print("+"+"-"*cols*5+"+")
def find_list_name():
    for i in l:
        for j in i:
            if j == a:
                return l.index(i),i.index(j)
row_a , col_a = find_list_name()
while 1:
    direction = random.choice(og)
    if (direction == 'up' and a in l[0]) or (direction == 'down' and a in l[(len(l)-1)]) or (direction == 'left' and col_a == 0) or (direction=='right' and col_a == (len(l)-1)):
        os.system('cls')
        grid()
        sleep(0.5)
        continue
    elif direction == 'up':
        l[row_a][col_a] = " "
        row_a -= 1
        os.system('cls')
        grid()
        sleep(0.5)
    elif direction == 'down':
        l[row_a][col_a] = " "
        row_a += 1
        os.system('cls')
        grid()
        sleep(0.5)
    elif direction == 'left':
        l[row_a][col_a] = " "
        col_a -= 1
        os.system('cls')
        grid()
        sleep(0.5)
    elif direction == 'right':
        l[row_a][col_a] = " "
        col_a += 1
        os.system('cls')
        grid()
        sleep(0.5)
    elif direction == 'top_right':
        l[row_a][col_a] = " "
        row_a -= 1
        col_a += 1
        os.system('cls')
        grid()
        sleep(0.5)
    elif direction == 'bottom_right':
        l[row_a][col_a] = " "
        row_a += 1
        col_a += 1
        os.system('cls')
        grid()
        sleep(0.5)
    elif direction == 'top_left':
        l[row_a][col_a] = " "
        col_a -= 1
        row_a -= 1 
        os.system('cls')
        grid()
        sleep(0.5)
    elif direction == 'bottom_left':
        l[row_a][col_a] = " "
        col_a -= 1
        row_a += 1
        os.system('cls')
        grid()
        sleep(0.5)
    

        
