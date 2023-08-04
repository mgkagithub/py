import random
from time import sleep
import os
import cv2
import math
cols = int(input("Enter no. of cols: "))
rows = cols
walls = math.ceil(((cols-2)/2))
history = []
first_wall = 1
wall_indices = [1]
for i in range(1,walls):
    first_wall+=2
    wall_indices.append(first_wall)
print(walls,wall_indices)
sleep(2)
a,row_a,col_a,rook,queen = '#',rows-1,0,['up','down','left','right'],['up','down','left','right','top_right','top_left','bottom_right','bottom_left']
l = [[" " for i in range(cols)] for j in range(rows)]
l[row_a][col_a] = a
for j in wall_indices:
    for i in range(0,cols-1):
        l[i][j] = '|'
for i in range(0,len(wall_indices),2):
        l[cols-1][wall_indices[i]] = '|'
        l[0][wall_indices[i]] = ' '
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
def end():
    if row_a == 0 and col_a == cols-1:
        return True
    else:
        return False
def check(row,col):
    if (row,col) in history:
        return 'repeat'
    else:
        return True
control_wtd = 1#int(input("-> enter 1 for random animal\n-> enter 2 for manual control\n-> "))
if control_wtd==1:
    movement_type = 1#int(input("-> enter 1 for Rook movement\n-> enter 2 for queen movement\n-> "))
while 1:
    if end() == True:
        print("The symbol has reached the end , program exiting...") 
        exit()
    else:
        if control_wtd==1:
            if movement_type == 1:
                direction_choice = rook
            else:
                direction_choice = queen
            direction = random.choice(direction_choice)
            if (direction == 'up' and a in l[0]) or (direction == 'down' and a in l[(cols-1)]) or (direction == 'left' and col_a == 0) or (direction=='right' and col_a == (cols-1)):
                os.system('cls')
                grid()
                print(history)
                pass                
            elif direction == 'up' and l[row_a-1][col_a]!='|':
                l[row_a][col_a] = " "
                row_a -= 1
                if check(row_a,col_a) == 'repeat':
                    pass
                else:
                    os.system('cls')
                    grid()
                    print(history)
                    sleep(1)
                    history.append((row_a,col_a))
            elif direction == 'down' and l[row_a+1][col_a]!='|':
                l[row_a][col_a] = " "
                row_a += 1
                if check(row_a,col_a) == 'repeat':
                    pass
                else:
                    os.system('cls')
                    grid()
                    print(history)
                    sleep(1)
                    history.append((row_a,col_a))
            elif direction == 'left' and l[row_a][col_a-1]!='|':
                l[row_a][col_a] = " "
                col_a -= 1
                if check(row_a,col_a) == 'repeat':
                    pass
                else:
                    os.system('cls')
                    grid()
                    print(history)
                    sleep(1)
                    history.append((row_a,col_a))
            elif direction == 'right' and l[row_a][col_a+1]!='|':
                l[row_a][col_a] = " "
                col_a += 1
                if check(row_a,col_a) == 'repeat':
                    pass
                else:
                    os.system('cls')
                    grid()
                    print(history)
                    sleep(1)
                    history.append((row_a,col_a))
            elif direction == 'top_right':
                #l[row_a][col_a] = " "
                l[row_a][col_a] = "="
                row_a -= 1
                col_a += 1
                os.system('cls')
                grid()
                sleep(1)
            elif direction == 'bottom_right':
                #l[row_a][col_a] = " "
                l[row_a][col_a] = "="
                row_a += 1
                col_a += 1
                os.system('cls')
                grid()
                sleep(1)
            elif direction == 'top_left':
                #l[row_a][col_a] = " "
                l[row_a][col_a] = "="
                col_a -= 1
                row_a -= 1 
                os.system('cls')
                grid()
                sleep(1)
            elif direction == 'bottom_left':
                #l[row_a][col_a] = " "
                l[row_a][col_a] = "="
                col_a -= 1
                row_a += 1
                os.system('cls')
                grid()
                sleep(1)
        elif control_wtd == 2:
            grid()
            if cv2.waitKey(1) & 0xFF == ord('w'):
                #l[row_a][col_a] = " "
                l[row_a][col_a] = "="
                row_a -= 1
                os.system('cls')
                grid()
                sleep(1)
            elif cv2.waitKey(1) & 0xFF == ord('s'):
                #l[row_a][col_a] = " "
                l[row_a][col_a] = "="
                row_a += 1
                os.system('cls')
                grid()
                sleep(1)
            elif cv2.waitKey(1) & 0xFF == ord('a'):
                #l[row_a][col_a] = " "
                l[row_a][col_a] = "="
                col_a -= 1
                os.system('cls')
                grid()
                sleep(1)
            elif cv2.waitKey(1) & 0xFF == ord('d'):
                #l[row_a][col_a] = " "
                l[row_a][col_a] = "="
                col_a += 1
                os.system('cls')
                grid()
                sleep(1)

    

        
