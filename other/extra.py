import random as r
import os
os.system('cls')
ccards = []
ccards_power = []
ccards_legendary = []
pcards = []
legendary_cards = ['+4- ','W- ']
power_cards = ['R-Y', 'S-Y','R-R','S-R','R-G','S-G','R-B','S-B','+4- ','W- ', '+2-Y', '+2-B','+2-G','+2-R']

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
r.shuffle(cards)
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
for i in range(0,10):
    ccards.append(shuffled_cards[i])
power_ccards = []
outcome_power_cards = []
len_ccards , len_power_ccards = 0,0
# ur cards(len of pcards -> color -> value) -> top card -> others 
def power_cards_diff():
    global ccards , ccards_power , power_cards , len_power_ccards , ccards_legendary
    print(f"initial set - {ccards}\nlen - {len(ccards)}")
    len_ccards = len(ccards)
    for i in ccards:
        if i in power_cards:
            ccards_power.append(i)
            ccards.remove(i)
    def check1():
        for i in ccards:
            if i in power_cards:
                power_cards_diff()
        return ccards , ccards_power
    check1()
    def check2():
        if len_ccards == len(ccards) + len(ccards_power):
            return False
        else:
            return True
    def true_legen():
        for i in ccards_power:
            if i in legendary_cards:
                ccards_legendary.append(i)
                ccards_power.remove(i)
        def check1():
            for i in ccards_power:
                if i in legendary_cards:
                    true_legen()
            return ccards , ccards_power , ccards_legendary
        check1()
        def check3():
            if len_ccards == len(ccards) + len(ccards_power) + len(ccards_legendary):
                return False
            else:
                return True  
        print(f"final set - {ccards} , {ccards_power}\nlen(ccards) - {len(ccards)}\nlen(power cards) - {len(ccards_power)}\nlen(legen cards) - {len(ccards_legendary)}\nlength error = {check3()}")
    true_legen() 
    print(ccards,ccards_power,ccards_legendary) 
    return ccards , ccards_power , ccards_legendary

def find_mode(lst):
    frequency_num = {}
    frequency_col = {}
    for num in lst:
        num = num.split('-')
        num = num[0]
        if num in frequency_num:
            frequency_num[num] += 1
        else:
            frequency_num[num] = 1
    for col in lst:
        col = col.split('-')
        col = col[1]
        if col in frequency_col:
            frequency_col[col] += 1
        else:
            frequency_col[col] = 1

    max_frequency_num = max(frequency_num.values())
    max_frequency_col = max(frequency_col.values())
    mode_num = [num for num, freq in frequency_num.items() if freq == max_frequency_num]
    mode_col = [col for col, freq in frequency_col.items() if freq == max_frequency_col]
    return mode_num , mode_col

def find_anti_mode(lst):
    frequency_num = {}
    frequency_col = {}
    for num in lst:
        num = num.split('-')
        num = num[0]
        if num in frequency_num:
            frequency_num[num] += 1
        else:
            frequency_num[num] = 1
    for col in lst:
        col = col.split('-')
        col = col[1]
        if col in frequency_col:
            frequency_col[col] += 1
        else:
            frequency_col[col] = 1

    min_frequency_num = min(frequency_num.values())
    min_frequency_col = min(frequency_col.values())
    mode_num = [num for num, freq in frequency_num.items() if freq == min_frequency_num]
    mode_col = [col for col, freq in frequency_col.items() if freq == min_frequency_col]
    return mode_num , mode_col

def verify_h():
    global top_card,pcards,shuffled_cards

    a = card_name.split('-')
    b = top_card.split('-')

    if card_name not in power_cards:
        if a[0]==b[0] or a[1]==b[1]:
            top_card = card_name

            if last_played == 'c':
                ccards.remove(card_name)
                card_deck.append(card_name)
                return ccards,card_deck

            else:
                pcards.remove(card_name)
                card_deck.append(card_name)
                return pcards,card_deck
        else:                                                                                                                                              

            print("Your first-card/card doesnt match the top card , try again")

    else:
        if last_played == 'c':    #c == computer , p == player

            if card_name == '+4- ':

                for i in range(4):

                    pcards.append(shuffled_cards[i])
                    top_card = card_name
                ccards.remove(card_name)
                card_deck.append(card_name)
                color = random.choice(['R','G','B','Y'])
                # try using mode 
                top_card = f"' '-{color}"
                return top_card,card_deck,ccards

            elif a[0]=='+2' and a[1]==b[1] or a[0]=='+2' and a[0]==b[0]:

                for i in range(2):
                    pcards.append(shuffled_cards[i])
                    top_card = card_name 
                card_deck.append(card_name)
                return top_card,card_deck

            elif a[0] == 'R' and a[1]==b[1] or a[0] == 'R' and b[0] == 'R':

                player_loop.reverse()
                ccards.remove(card_name)   
                top_card = card_name
                card_deck.append(card_name)
                return top_card,card_deck

            elif a[0] == 'S' and a[1]==b[1] or a[0] == 'S' and b[0] == 'S':

                player_loop.reverse()
                ccards.remove(card_name)
                top_card = card_name
                card_deck.append(card_name)
                print(card_name)
                return top_card,card_deck

            elif a[0] == 'W' or a[0] == ' ':

                top_card = card_name
                color = random.choice(['R','G','B','Y'])
                top_card = f"' '-{color}"
                card_deck.append(card_name)
                return top_card ,card_deck

        else:

            if card_name == '+4' and card_name[0]==top_card[0] or a[0] == " ":
                color = input("Enter color - R , G , B or Y:\n")
                color = input("Enter a color:\n")
                color = color.upper()   

                for i in range(4):
                    ccards.append(shuffled_cards[i])
                    shuffled_cards.remove(shuffled_cards[i])
                pcards.remove(card_name)
                card_deck.append(card_name)
                top_card = f"' '-{color}"
                return top_card,card_deck

            elif a[0]=='+2' or a[1]==b[1]:

                pcards.remove(card_name)
                for i in range(2):
                    ccards.append(shuffled_cards[i])
                    top_card = card_name
                card_deck.append(card_name)
                return top_card,card_deck

            elif a[0] == 'R' and a[1]==b[1] or a[0] == 'R' and b[0] == 'R':

                player_loop.reverse()
                pcards.remove(card_name)
                top_card = card_name
                card_deck.append(card_name)
                return top_card,card_deck

            elif a[0] == 'S' and a[1]==b[1] or a[0] == 'S' and b[0] == 'S':

                player_loop.reverse()
                pcards.remove(card_name)
                top_card = card_name
                card_deck.append(card_name)
                return top_card,card_deck

            elif a[0] == 'W' or a[0] == ' ':

                color = input("Enter a color:\n")
                color = color.upper()
                top_card = f"' '-{color}"
                pcards.remove(card_name)
                card_deck.append(card_name)
                return top_card ,card_deck


def human():
    global pcards , top_card
    outcome = []
    top_card_config = top_card.split('-')
    ppcards = []
    if len(pcards)>=5:
        for i in range(len(pcards)):
            if ccards[i].split('-')[0] == top_card_config[0] or ccards[i].split('-')[1] == top_card_config[1]:
                ppcards.append(ccards[i])
    #    for i in range(len(ccards)):
    #        if ccards[i].split('-')[0] == top_card_config[0] or ccards[i].split('-')[1] == top_card_config[1]:
    #            ppcards.append(ccards[i]) 

        def find_mode(lst):
            frequency = {}
            for num in lst:
                num = num.split('-')
                num = num[0]
                if num in frequency:
                    frequency[num] += 1
                else:
                    frequency[num] = 1
            
            max_frequency = max(frequency.values())
            mode = [num for num, freq in frequency.items() if freq == max_frequency]
            
            return mode

        mode = find_mode(pcards)
        anti_mode = find_anti_mode(pcards)
        for i in range(len(ccards)):
            if ccards[i].split('-')[0] == mode[0]:
                outcome.append(ccards[i])
        for i in range(len(outcome)):
            if len(outcome) <= 0:
                deck(ccards)
                return ccards
            else:
                if outcome[i].split('-')[1] == top_card_config[1]:
                    outcome[i],outcome[0] = outcome[0],outcome[i]
        print(f"outcome is {outcome}")
        for i in outcome:
            print(i)
    else:
        power_comp()

def play_best_stack():
    global ccards , ccards_power
    outcome = []
    top_card_config = top_card.split('-')
    ppcards = []
    if len(pcards)>=5:
        for i in range(len(ccards)):
            if ccards[i].split('-')[0] == top_card_config[0] or ccards[i].split('-')[1] == top_card_config[1]:
                ppcards.append(ccards[i])
# 5<pcards = normal , wild , +2 , skip , reverse 
        def find_mode(lst):
            frequency = {}
            for num in lst:
                num = num.split('-')
                num = num[0]
                if num in frequency:
                    frequency[num] += 1
                else:
                    frequency[num] = 1
            
            max_frequency = max(frequency.values())
            mode = [num for num, freq in frequency.items() if freq == max_frequency]
            
            return mode

        mode = find_mode(ccards)
        for i in range(len(ccards)):
            if ccards[i].split('-')[0] == mode[0]:
                outcome.append(ccards[i])
        for i in range(len(outcome)):
            if len(outcome) <= 0:
                deck(ccards)
                return ccards
            else:
                if outcome[i].split('-')[1] == top_card_config[1]:
                    outcome[i],outcome[0] = outcome[0],outcome[i]
        print(f"outcome is {outcome}")
        for i in outcome:
            if len(outcome)>0:
                print(i)
            else:
                deck(ccards)
    else:
        pass
    #add +4 and wild card - only color change n dont add a card

def power_comp():
    global ccards , top_card , power_ccards , outcome_power_cards
    outcome = []
    top_card_config = top_card.split('-')
    ppcards = []
    for i in range(len(ccards)):
        if ccards[i].split('-')[0] == top_card_config[0] or ccards[i].split('-')[1] == top_card_config[1]:
            ppcards.append(ccards[i])
#    for i in range(len(ccards)):
#        if ccards[i].split('-')[0] == top_card_config[0] or ccards[i].split('-')[1] == top_card_config[1]:
#            ppcards.append(ccards[i]) 

    mode = find_mode(ccards)
    for i in range(len(ccards)):
        if ccards[i].split('-')[0] == mode[0]:
            outcome.append(ccards[i])
    for i in range(len(outcome)):
        if len(outcome) <= 0:
            deck(ccards)
            return ccards
        else:
            if outcome[i].split('-')[1] == top_card_config[1]:
                outcome[i],outcome[0] = outcome[0],outcome[i]

    print(f"outcome is {outcome}")
power_cards_diff()
value1 , color1 = find_mode(ccards)
value2 , color2 = find_anti_mode(ccards)
print("value 1 , color1 = ",value1,color1)
print("value 2 , color2 = ",value2,color2)

def deck_1():
    pass
def deck_m():
    pass
def legendary_c():
    pass
def s_r_c():
    pass
def s_r_m():
    pass
def s_r_p():
    pass
def n_l_p():
    pass
def l_p():
    pass
def o_s_r():
    pass
def req_info():
    pass
def comp():
    moves = [deck_1(),deck_m(),legendary_c(),s_r_c(),s_r_m(),s_r_p(),n_l_p(),l_p(),o_s_r()]
    print(moves)
comp()





