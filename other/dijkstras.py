top_card = input("Enter the top card: \n")
pcards = ['0-Y', '1-R', '2-B', '3-G', '+2-B','0-R','1-R','2-R','3-R','0-B']
outcome = []

def max_cards(card):
    global pcards , outcome , top_card , ppcards
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
max_cards(top_card)