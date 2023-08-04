import random
def sort_ccards(ccards, input_card):
    # Split 'R-' and 'S-' cards into separate lists
    r_cards = [card for card in ccards if card.startswith('R-')]
    s_cards = [card for card in ccards if card.startswith('S-')]

    # Sort both lists by color (B)
    r_cards.sort(key=lambda card: card.split('-')[1])
    s_cards.sort(key=lambda card: card.split('-')[1])

    # Find the index of the input card in the sorted 'R-' or 'S-' list
    input_color = input_card.split('-')[1]
    if input_card.startswith('R-'):
        input_index = next((i for i, card in enumerate(r_cards) if card.endswith(input_color)), None)
    else:
        input_index = next((i for i, card in enumerate(s_cards) if card.endswith(input_color)), None)

    # Merge the two lists to form the final sorted list
    if input_index is not None:
        if input_card.startswith('R-'):
            sorted_ccards = r_cards[input_index:] + s_cards + r_cards[:input_index]
            if r_cards and s_cards:
                # Check if we need to join the last 'R-' card and the first 'S-' card with the same color
                if r_cards[-1].endswith(input_color) and s_cards[0].endswith(input_color):
                    sorted_cards = r_cards+ s_cards
        else:
            sorted_ccards = s_cards[input_index:] + r_cards + s_cards[:input_index]
            if s_cards and r_cards:
                # Check if we need to join the last 'S-' card and the first 'R-' card with the same color
                if s_cards[-1].endswith(input_color) and r_cards[0].endswith(input_color):
                    s_cards = s_cards+r_cards
    else:
        sorted_ccards = s_cards + r_cards

    return sorted_ccards

# Test data
ccards = []
d = {}
skip_reverse = ['R-R','R-R','S-R','S-R',
                'R-G','R-G','S-G','S-G',
                'R-B','R-B','S-B','S-B',
                'R-Y','R-Y','S-Y','S-Y']
random.shuffle(skip_reverse)
for i in range(5):
    ccards.append(skip_reverse[i])
input_card = input("Enter top card: \n")

# Call the function and print the result
sorted_cards = sort_ccards(ccards, input_card)
print(sorted_cards)
