import random as r
from extra import find_mode , find_anti_mode
pcards = []
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
top_card_config = []
r.shuffle(cards)
shuffled_cards = cards
for i in range(0,20):
    pcards.append(shuffled_cards[i])
print(pcards)
player_loop = ['p','c']
outcome = []
top_card = input("Enter the top card: \n")
if top_card == '+4- ' or top_card == 'W- ':
    color_wild_4 = input("Enter a color: R , G , B, Y :\n")
    color_wild_4 = color_wild_4.upper()
    top_card_config = [' ' ,color_wild_4]

def max_cards(card):
    global pcards , outcome , top_card , ppcards , top_card_config
    top_card_config = top_card.split('-')
    ppcards = []
    for i in range(len(pcards)):
        if pcards[i].split('-')[0] == top_card_config[0] or pcards[i].split('-')[1] == top_card_config[1]:
            ppcards.append(pcards[i])

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
    for i in range(len(pcards)):
        if pcards[i].split('-')[0] == mode[0]:
            outcome.append(pcards[i])
    for i in range(len(outcome)):
        if outcome[i].split('-')[1] == top_card_config[1]:
            outcome[i],outcome[0] = outcome[0],outcome[i]

    print(outcome)

# while True:
#     for i in player_loop:
#         if i == 'p':
#             card = input("what would u play:\n")
#         else:
max_cards(pcards)

# write for +4 and w- for humans and for comp using anti_mode and mode 
# use 'pass' for skipping turns n stuff