import random as r
import os
os.system('cls')
ccards = []
ccards_power = []
ccards_legendary = []
ccards_skip_reverse = []
pcards = [] 
outcome = []
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
                return "no error"
            else:
                return "error"
        print(f"final set - \nlen(ccards) - {len(ccards)}\nlen(power cards) - {len(ccards_power)}\nlen(legen cards) - {len(ccards_legendary)}\nlen(S and R) - {len(ccards_skip_reverse)}\nlength error = {check4()}")
    skip_reverse_only()
    # print(ccards , ccards_power,ccards_skip_reverse,ccards_legendary)
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
power_cards_diff()
print(ccards_skip_reverse)
mode = find_mode(ccards_skip_reverse)
for i in range(len(ccards_skip_reverse)):
    if ccards_skip_reverse[i].split('-')[0] == mode[0]:
        outcome.append(ccards_skip_reverse[i])
for i in range(len(outcome)):
    if outcome[i].split('-')[1] == top_card_config[1]:
        outcome[i],outcome[0] = outcome[0],outcome[i]
print(outcome)