import random as r 
import os
human_left , human_right , comp_left , comp_right = 1,1,1,1
os.system('cls')
print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
def win():
    global hp , cp
    if human_left == 0 and human_right == 0:
        print(f"The computer has won and beat you in {cp} move(s)")
        exit()
        return c
    elif comp_left == 0 and comp_right == 0:
        print(f"You beat the computer and won in {hp} move(s)")
        exit()
        return h
hp,cp = 0,0
while True:
    for i in ['h','c']:
        if i == 'h':
            win()
            hp += 1
            choice = input("Would u like to:\n\ns - switch values\nd - divide values\nt - tap the computer\nq - quit?")
            if choice == 's':
                human_left,human_right = human_right,human_left
                print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
            elif choice == 'd':
                hand = input("which hand would u like to add the value to?\nEnter L for left and R for right:\n")
                hand = hand.upper()
                if hand == 'L':
                    hand = human_left
                else:
                    hand = human_right
                value = int(input("Enter the value to be added:\n"))
                if value%5 == 0:
                    print("Invalid value")
                elif (hand - value) < 0:
                    print("Invalid value")
                else:
                    if hand == human_left:
                        human_left,human_right = human_left+value,human_right-value
                        print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
                    else:
                        human_left,human_right = human_left-value,human_right+value
                        print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
            elif choice == 'q':
                os.system('cls')
                print("Game has been quit.")
                exit()
            elif choice == 't':        
                comp_hand = input("which computer hand would u like to tap?\nEnter L for left and R for right:\n")
                human_hand = input("choose the hand you would use to tap\nEnter L for left and R for right:\n")
                comp_hand , human_hand = comp_hand.upper() , human_hand.upper()
                if comp_hand == 'L': 
                    if human_hand == 'L':
                        comp_left = (comp_left+human_left)%5
                        print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
                    else:
                        comp_left = (comp_left+human_right)%5
                        print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
                elif comp_hand == 'R':
                    if human_hand == 'L':
                        comp_right = (comp_right+human_left)%5
                        print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
                    else:
                        comp_right = (comp_right+human_right)%5
                        print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
        elif i == 'c':
            win()
            cp += 1
            choice = r.choice(['t','t','t','t','d','d','s'])
            if choice == 'd':
                print("computer divided between hands")
                c_hand = r.choice(['L','R'])
                if c_hand == 'L' and comp_right>0:
                    rannum = r.randint(1, comp_right)
                    comp_left,comp_right = comp_left+rannum , comp_right - rannum
                    print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
                elif c_hand == 'R' and comp_left>0:
                        rannum = r.randint(1, comp_left)
                        comp_left,comp_right = comp_left-rannum , comp_right + rannum
                        print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
            elif choice == 's':
                    print("computer has decided to switch")
                    comp_left,comp_right = comp_right,comp_left
                    print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")               
            elif choice == 't':
                print("the computer has decided to tap you")
                c_hand = r.choice(['L','R'])
                human_hand = r.choice(['L','R'])
                if c_hand == 'L' and comp_left>0: 
                    if human_hand == 'L':
                        if human_left>0:
                            human_left = (human_left+comp_left)%5
                            print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")                        
                        else:
                            human_right = (human_right+comp_left)%5
                            print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
                elif c_hand == 'R' and comp_right>0:
                    if human_hand == 'R':
                        if human_right>0:
                            human_right = (human_right+comp_left)%5
                            print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")
                        else:
                            human_left = (human_left+comp_right)%5
                            print(f"\n\n    L   R\n\nC - {comp_left} , {comp_right}\n\nH - {human_left} , {human_right}\n\n")

                
















