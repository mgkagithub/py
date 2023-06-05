import random as r 
import os
human_left , human_right , comp_left , comp_right = 1,1,1,1
while True:
    print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
    for i in ['h','c']:
        if i == 'h':
            choice = input("Would u like to \ns - switch values\nd - divide values\nt - tap the computer\nq - quit?")
            if choice == 's':
                human_left,human_right = human_right,human_left
                print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                
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
                elif (hand - value) < 0 or (hand - value) < 0:
                    print("Invalid value")
                else:
                    if hand == human_left:
                        human_left,human_right = human_left+value,human_right-value
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
                    else:
                        human_left,human_right = human_left-value,human_right+value
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
            elif choice == 'q':
                print("Game has been quit.")
                exit()
            elif choice == 't':        
                comp_hand = input("which computer hand would u like to tap?\nEnter L for left and R for right:\n")
                human_hand = input("choose the hand you would use to tap\nEnter L for left and R for right:\n")
                comp_hand , human_hand = comp_hand.upper() , human_hand.upper()
                print(comp_hand,human_hand)
                if comp_hand == 'L': 
                    if human_hand == 'L':
                        comp_left = (comp_left+human_left)%5
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
                    else:
                        comp_left = (comp_left+human_right)%5
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
                elif comp_hand == 'R':
                    if human_hand == 'L':
                        comp_right = (comp_right+human_left)%5
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
                    else:
                        comp_right = (comp_right+human_right)%5
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
        elif i == 'c':
            choice = r.choice(['t','t','d','d','s'])
            if choice == 'd':
                print("computer divided between hands")
                c_hand = r.choice(['L','R'])
                if c_hand == 'L' and comp_right>0:
                    rannum = r.randint(1, comp_right)
                    comp_left,comp_right = comp_left+rannum , comp_right - rannum
                    print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                elif c_hand == 'R' and comp_left>0:
                        rannum = r.randint(1, comp_left)
                        comp_left,comp_right = comp_left-rannum , comp_right + rannum
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
            elif choice == 's':
                    print("computer has decided to switch")
                    human_left,human_right = human_right,human_left
                    print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                    
            elif choice == 't':
                print("the computer has decided to tap you")
                c_hand = r.choice(['L','R'])
                human_hand = r.choice(['L','R'])
                if c_hand == 'L': 
                    if human_hand == 'L':
                        human_left = (human_left+comp_left)%5
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
                    else:
                        human_left = (human_left+comp_right)%5
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
                elif c_hand == 'R':
                    if human_hand == 'L':
                        human_right = (human_right+comp_left)%5
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")
                        
                    else:
                        human_right = (human_right+comp_right)%5
                        print(f"    L   R\nC - {comp_left} , {comp_right}\nH - {human_left} , {human_right}")

                
















