# this file was created by Matthew Gustafson 
# https://www.youtube.com/watch?v=yJz2at4Hco4

# Blackjack or 21 game

import random
# The Planning Phase
 # Dealer cards
dealer_cards = []
 # Player cards
player_cards = []

 # Display cards
#Dealer cards 
while len(dealer_cards) !=2:
    dealer_cards.append(random.randint(1,11))
    # This deals the cards for the dealer 
    if len(dealer_cards) ==2:
        print("The dealer is showing a:", dealer_cards[1])
        # This shows us only one of the dealer cards by only showing index [1] 

#Player cards 
while len(player_cards) !=2:
    player_cards.append(random.randint(1,11))
    # This deals the cards for the player 
    if len(player_cards) ==2:
        print("You have a:", player_cards)
        # This shows us only one of the dealer cards by only showing index [1] 
 # Sum of dealer cards
if sum(dealer_cards) == 21:    
     print("The dealer has a blackjack!")
elif sum(dealer_cards) > 21:
     print("The dealer has busted. You Win!")
 # Sum of player cards
while sum(player_cards) < 21: 
     action_taken = str(input("Do you want to hit or stand?  "))
     if action_taken == "hit" or "Hit":
            player_cards.append(random.randint(1,11))
            print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
     else:
         print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
         print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
         if sum(dealer_cards) > sum(player_cards):
             print("The dealer wins!")
         else:
             print("You win!")
             break

if sum(player_cards) > 21:
    print("You busted. The dealer wins!") 
elif sum(player_cards) == 21: 
    print("You have a blackjack! Congrats! You win!")

 # Compare sum of cards between D v P 
 # If P card sum is greater than 21 = Bust
 # If P card sum is less than 21 = Option hit or stand
 # If P options to stand compare sum of cards between D v P
 # If P sum < 21 & > D sum then P wins!
 # If P sum < D sum then P loses!