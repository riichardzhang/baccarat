# Return random card where 10, J, Q and K are the same value.

import random

# 11 = J, 12 = Q and 13 = K
def randomCard():
    card_selection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    return random.choice(card_selection)

def cardToValue(card):
    if card == 11 or card == 12 or card == 13:
        card = 10

    return card