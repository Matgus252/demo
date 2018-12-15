# this file was created by Matthew Gustafson 
# https://www.youtube.com/watch?v=yJz2at4Hco4

# I copied code from the above youtube video 

    # In order to make it my own with the help of Mr. Cozort I inputed ... 
         # the ability for the dealer to hit until he has 17 or more (see lines 68-79)
         # the end game evaluation (see lines 81-96)
         # and the player/dealer having a blackjack (see lines 40-47)

    # I also changed the words used in all print statements 

# In this project I developed a better sence of coding especially termonology of how certain statements work including (while, if, and elif)

# This creates the deck
import random
dealer_cards = []
player_cards = []

# This deals the cards for the player
while len(player_cards) !=2:
    player_cards.append(random.randint(1,11))
    # This stops the player from playing when dealt two 11's
    if sum(player_cards) == 22:
        print("GAME ERROR! Please reset.")
    # This shows the player what number he has with what cards 
    elif len(player_cards) ==2:
        print("You were dealt: " + str(sum(player_cards)) + " with the cards" , player_cards )

# This deals the cards for the dealer
while len(dealer_cards) !=2:
    dealer_cards.append(random.randint(1,11))
    # This stops the player from playing when the dealer is dealt two 11's
    if sum(dealer_cards) == 22:
        print("GAME ERROR! Please reset.")
    # This shows the player one of the dealer's cards 
    elif len(dealer_cards) == 2:
        print("The dealer is showing a: ", dealer_cards[1])

# This evaluates if the dealer has a blackjack
while sum(dealer_cards) == 21:    
    print("The dealer has a blackjack!")
    break
# This evaluates if the player has a blackjack
while sum(player_cards) == 21: 
    print("You have a blackjack! Congrats! You win!")
    break

# This provides the player with the option to hit or stand 
while True: 
    action_taken = str(input("Do you want to hit or stand?  "))
    # This recalls the action that the player chose 
    print("You chose to" , action_taken)
    if action_taken == "hit":
        # This says if the player choses to hit it will append a card
        player_cards.append(random.randint(1,11))
        # This will tell the player his or her current total after hitting 
        print("Current total = " + str(sum(player_cards)) + " from these cards", player_cards)
        # This will stop the game if the player busts 
    if sum(player_cards) > 21:
        print("You busted with a " + str(sum(player_cards)))
        # Due to the while loop as long as the player doesn't bust than it will ask the initial question of hit or stand 
        break
        # This allows the player to stand 
    if  action_taken == "stand":
        break

# This is the next step of the game when the player chooses to stand 
while action_taken == "stand":
    # This flips the other dealer card over and tells the player what the dealer has 
    print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
    print("The dealer currently has " + str(sum(dealer_cards)))
    # This makes sure that the dealer is appended a card until he is at or above 17 
    if sum(dealer_cards) <= 17:
        dealer_cards.append(random.randint(1,11))
    # Once the dealer has reached or gone above 17 this will restate what the player and dealer has
    else:
        print("You had " + str(sum(player_cards)) + " the dealer has " + str(sum(dealer_cards)))
        break
            
# This evaluates the end game 
# This evaluates if the dealer has busted 
if sum(dealer_cards) > 21:
    print("The dealer has busted. You Win!")
# This evaluates if the player wins 
elif (sum(dealer_cards) <= 21) < (sum(player_cards) <= 21):
    print("You WIN!")
# This evaluates if the dealer wins 
elif (21 >= sum(player_cards)) < (sum(dealer_cards) <= 21):
    print("The dealer wins!")
# This evaluates a push 
elif sum(dealer_cards) == sum(player_cards):
    print("Push, keep your money!")
# This tells me if something went wrong during the evaluation 
    print("The coder messed up this portion of the game. Read the line above and determine whether or not you won.")


# if sum(dealer_cards) > 21:
#     print("The dealer has busted. You Win!")
# elif sum(dealer_cards) == sum(player_cards):
#     print("Push, keep your money!")

# while (21 >= sum(player_cards)) + (sum(dealer_cards) <= 21):
#     if (sum(dealer_cards) <= 21) < (sum(player_cards) <= 21):
#         print("You WIN!")
#         break
#     elif (21 >= sum(player_cards)) < (sum(dealer_cards) <= 21):
#         print("The dealer wins!")
#         break