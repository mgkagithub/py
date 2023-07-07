import random as r
import os
import statistics
os.system('cls')
ccards = []
ccards_power = []
ccards_legendary = []
ccards_skip_reverse = []
pcards = [] 
legendary_cards = ['+4- ','W- ']
power_cards = ['R-Y', 'S-Y','R-R','S-R','R-G','S-G','R-B','S-B','+4- ','W- ', '+2-Y', '+2-B','+2-G','+2-R']

skip_reverse = ['R-R','R-R','S-R','S-R',
                'R-G','R-G','S-G','S-G',
                'R-B','R-B','S-B','S-B',
                'R-Y','R-Y','S-Y','S-Y']
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
for i in range(0,20):
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
    true_legen()
    def skip_reverse_only():
        for i in ccards_power:
            if i in skip_reverse:
                ccards_skip_reverse.append(i)
                ccards_power.remove(i)
        def check1():
            for i in ccards_power:
                if i in skip_reverse:
                    skip_reverse_only()
            return ccards , ccards_power , ccards_legendary , ccards_skip_reverse
        check1()
        def check4():
            if len_ccards == len(ccards) + len(ccards_power) + len(ccards_legendary) + len(ccards_skip_reverse):
                return True
            else:
                return False
        print(f"final set - \nlen(ccards) - {len(ccards)}\nlen(power cards) - {len(ccards_power)}\nlen(legen cards) - {len(ccards_legendary)}\nlen(S and R) - {len(ccards_skip_reverse)}\nlength error = {check4()}")
    skip_reverse_only()
    print(ccards , ccards_power,ccards_skip_reverse,ccards_legendary)
    return ccards , ccards_power , ccards_legendary , ccards_skip_reverse

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

def deck_1(ccards,deck,top_card):
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
    all_cards = shuffled_cards
    comp_cards = ccards
    top_card = top_card
    power_cards = power_cards
    legendary_cards = legendary_cards
    mode_ccards = find_mode(comp_cards)
    anti_mode_ccards = find_anti_mode(comp_cards)

    pass
def comp():
    moves = [deck_1(),deck_m(),legendary_c(),s_r_c(),s_r_m(),s_r_p(),n_l_p(),l_p(),o_s_r()]
    print(max_move := max(moves))
    def move(max_move):
        dict1

    print(moves)
power_cards_diff()





