import random 

dealer_cards = []
player_card = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len (dealer_cards) == 2:
        print ("The dealer is showing a ", )