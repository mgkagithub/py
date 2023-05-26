ccards = ['+2-Y', '+2-B','+2-G','+2-R','W- ','+4- ','+4- ','+4- ']
test_cards = ['0-Y','1-R','2-B','3-G','+2-B','0-Y','5-R','3-B','9-G','+2-B','+4- ','W- ']
pcards = ['+2-Y', '+2-B','+2-G','+2-R','W- ','+4- ','+4- ','+4- ']
power_cards = ['R-Y', 'S-Y','R-R','S-R','R-G','S-G','R-B','S-B','+4- ','W- ', '+2-Y', '+2-B','+2-G','+2-R']
power_ccards = []
outcome_power_cards = []

# ur cards(len of pcards -> color -> value) -> top card -> others 

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
    print(mode_num , mode_col)
    return mode_num , mode_col

def find_anti_mode(lst):
    frequency = {}
    for num in lst:
        num = num.split('-')
        num = num[0]
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    min_frequency = min(frequency.values())
    anti_mode = [num for num, freq in frequency.items() if freq == min_frequency]
    print(anti_mode)
    return anti_mode

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

def computer():
    global ccards , top_card , pcards 
    outcome = []
    top_card_config = top_card.split('-')
    ppcards = []
    if len(pcards)>=5:
        for i in range(len(ccards)):
            if ccards[i].split('-')[0] == top_card_config[0] or ccards[i].split('-')[1] == top_card_config[1]:
                ppcards.append(ccards[i])
#    for i in range(len(ccards)):
#        if ccards[i].split('-')[0] == top_card_config[0] or ccards[i].split('-')[1] == top_card_config[1]:
#            ppcards.append(ccards[i]) 
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
value , color = find_mode(test_cards)
print(value,color)