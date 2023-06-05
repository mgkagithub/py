import random
import os
import time
os.system("cls")
#os.system("cls")

time.sleep(1)
def print_cards(pcards , ccards):
    global pcards , ccards , top_card , player_loop
    print("###########################################################")
    print()
    print("Card history/deck - ",card_deck)
    print()
    if win() == 'Comp':
        break
    elif win() == 'player':
        break
    for i in player_loop:
        if i=='p':
            check_pile(pcards)
            #os.system("cls")
            x = str(pcards).replace("'","")
            y = x.replace("[","")
            z = y.replace("]","")
            top_card_config = top_card.split('-')
            print("###########################################################")
            #os.system("cls")
            print()
            print("-> Top card value - {}\n-> Top card color - {}".format(top_card_config[0],top_card_config[1]))
            print()
            print('+-----+')
            print(f'|{top_card_config[1]}    |')
            print(f'|  {top_card_config[0]}  |')
            print(f'|    {top_card_config[1]}|')
            print('+-----+')
            print()
            print("player cards -")
            print()
            print('+-----+',end='')
            for i in range(len(pcards)-1):
                print('--+',end='')
            print()
            print(f"|{pcards[0].split('-')[-1]}    |",end='')
            for i in range(1,len(pcards)):
                if pcards[i].split('-')[0] in ('+2','+4'):
                    print(f"{pcards[i].split('-')[0]}|",end='')
                else:
                    print(f" {pcards[i].split('-')[0]}|",end='')
            print()
            if pcards[0].split('-')[0] in ('+2','+4'):
                print(f"| {pcards[0].split('-')[0]}  |",end='')
            else:
                print(f"|  {pcards[0].split('-')[0]}  |",end='')
            for i in range(1,len(pcards)):
                print('  |',end='')
            print()
            print(f"|    {pcards[0].split('-')[-1]}|",end='')
            for i in range(1,len(pcards)):
                print(f' {pcards[i][-1]}|',end='')
            print()
            print('+-----+',end='')
            for i in range(len(pcards)-1):
                print('--+',end='')
            print()                       
            print()
            print(f"Your cards [{len(pcards)}] -",pcards)
            print()
            print(f"Computer cards [{len(ccards)}] -",ccards)
            print()
            print("###########################################################")
            print()
cards = [

        '0-R','1-R','2-R','3-R','4-R','5-R','6-R','7-R','8-R','9-R',
        '1-R','2-R','3-R','4-R','5-R','6-R','7-R','8-R','9-R',
        
       
        '0-G','1-G','2-G','3-G','4-G','5-G','6-G','7-G','8-G','9-G', 
        '1-G','2-G','3-G','4-G','5-G','6-G','7-G','8-G','9-G', 
        

        '0-B','1-B','2-B','3-B','4-B','5-B','6-B','7-B','8-B','9-B', 
        '1-B','2-B','3-B','4-B','5-B','6-B','7-B','8-B','9-B', 
        

        '0-Y','1-Y','2-Y','3-Y','4-Y','5-Y','6-Y','7-Y','8-Y','9-Y', 
        '1-Y','2-Y','3-Y','4-Y','5-Y','6-Y','7-Y','8-Y','9-Y', 
        
        'W- ','+2-R','+2-R','+4- ','R-R','R-R','S-R','S-R',
        'W- ','+2-G','+2-G','+4- ','R-G','R-G','S-G','S-G',
        'W- ','+2-B','+2-B','+4- ','R-B','R-B','S-B','S-B',
        'W- ','+2-Y','+2-Y','+4- ','R-Y','R-Y','S-Y','S-Y'

        ]
        
etc = ['W- ','+2-R','+2-R','+4- ','R-R','R-R','S-R','S-R','W- ','+2-G','+2-G','+4- ','R-G','R-G','S-G','S-G','W- ','+2-B','+2-B','+4- ','R-B','R-B','S-B','S-B','W- ','+2-Y','+2-Y','+4- ','R-Y','R-Y','S-Y','S-Y']
card_starts = [0,1,2,3,4,5,6,7,8,9,'+2','+4','S','R','W']
legendary_cards = ['+4 -','W- ']
non_legendary_power_cards = [ '+2-Y', '+2-B','+2-G','+2-R','R-Y', 'S-Y','R-R','S-R','R-G','S-G','R-B','S-B']
power_cards = ['R-Y', 'S-Y','R-R','S-R','R-G','S-G','R-B','S-B','+4 -','W- ', '+2-Y', '+2-B','+2-G','+2-R']

card_deck = []
pcards = []
#pcards = ['0-Y','1-R','2-B','3-G','+2-B']
plus_cards = []
ccards = []
#ccards = ['+2-Y', '+2-B','+2-G','+2-R']
shuffled_cards = []
last_played = random.choice(['p','c'])
random.shuffle(cards)
shuffled_cards = cards
for i in shuffled_cards:
    top_card = ' '
    if shuffled_cards[0] not in power_cards:
        a = shuffled_cards[0]
        top_card = a
        break
    else:
        shuffled_cards.pop(0)
        shuffled_cards.append(shuffled_cards[0])
        top_card = shuffled_cards[1]
        continue
player_loop = ['p','c']
os.system("cls")
g = 0
while True:
    #time.sleep(5)
    print_cards()
    for i in player_loop:
        if i == 'p':

            wtd = input("what would u like to do ?\n\n> Play a card - Just enter the position of the card (order starts from 1)\n> d - gives you the top card from the deck\n> e - done playing? use this to exit.\n\n-> ")
            
            if wtd=='d':
                deck(pcards)
            elif wtd=='e':
                os.system("cls")
                print("Thanks for playing!")
                exit()
            else:
                g = int(wtd)
                card_played = pcards[g-1]
                verify(card_played,last_played)
            print()
            
        elif i == 'c':
            print()
            print(top_card)
            print()
            print("Computers Turn")
            print()
            computer()
            
        continue