#importing random to get random cards
import random

#initialise deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4


#deal cards
def deal(deck):
    hand_user = []
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
        #assigning 11,12,13,14 as Jack,Queen,King and Ace.
	    if card == 11:card = "Jack"
	    if card == 12:card = "Queen"
	    if card == 13:card = "King"
	    if card == 14:card = "Ace"

        #adding all the cards assigned to the list
	    hand_user.append(card)
    #returning list of cards = deck of user
    return hand_user


#if User wants to Play again or not
def play_again():

    ask_again = input("Do you want to play again? (Y/N) : ").lower()
    if ask_again == "y":

        #reset Values for a new game.
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()


	#exitng
    else:
        #Game Over
	    print("Okay,Bye!")
	    exit()

#total_in_hand Calculator 
def total_in_hand(hand):
    total_in_hand = 0
    for card in hand:
	    if card == "Jack" or card == "Queen" or card == "King":
	        total_in_hand+= 10
	    elif card == "Ace":
	        if total_in_hand >= 11: total_in_hand+= 1
	        else: total_in_hand+= 11
	    else: total_in_hand += card
    return total_in_hand


#condition where user asks to hit them with with one more card
def hit(hand):
	card = deck.pop()
	if card == 11:card = "Jack"
	if card == 12:card = "Queen"
	if card == 13:card = "King"
	if card == 14:card = "Ace"
	hand.append(card)
	return hand


#final Results to see dealer and your card
def print_results(dealer_hand, player_hand):
    #clear()
	print("\n\nThe dealer has a " + str(dealer_hand) + " for a Total of " + str(total_in_hand(dealer_hand)))
	print("You have a " + str(player_hand) + " for a Total of " + str(total_in_hand(player_hand)))


# If you get sum of cards as 21 you get a blackjack
def blackjack(dealer_hand, player_hand):
	if total_in_hand(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print ("\nCongratulations! You got a Blackjack!\n")
		play_again()
	elif total_in_hand(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print ("\nSorry, you lose. The dealer got a blackjack.\n")
		play_again()


#Other cases to compare user and computers deck
def score(dealer_hand, player_hand):
    # If USer get sum of cards as 21 you get a blackjack
    if total_in_hand(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")

    # If Computer get sum of cards as 21 you get a blackjack
    elif total_in_hand(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)		
        print ("Sorry, you lose. The dealer got a blackjack.\n")

    #Lost because sum got larger than 21
    elif total_in_hand(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry. You busted. You lose.\n")

    #Computer Lost because sum got larger than 21   
    elif total_in_hand(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)			   
        print ("Dealer busts. You win!\n")

    #Lost because your Sum is smaller than that of dealer
    elif total_in_hand(player_hand) < total_in_hand(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")

    #Computer Lost because your Sum is smaller than that of dealer
    elif total_in_hand(player_hand) > total_in_hand(dealer_hand):
        print_results(dealer_hand, player_hand)			   
        print ("Congratulations. Your score is higher than the dealer. You win\n")		


def game():
    choice = 0
    #GAME START
    print ("**********************WELCOME TO BLACKJACK!*************************\n\n")

    #making two decks , one for user and one for computer
    dealer_hand = deal(deck)
    player_hand = deal(deck)


    #start if user choose q while loop ends
    while choice != "q":

        #Menu to enter choice to see rules or play game or quit
        print("Enter a Choice.")
        main_choice =int(input('1.Enter 1 to See the Rules.\n2.Enter 2 to play Game.\n3.Enter 3 to Quit'))


        #user chooses to see the Rules
        if(main_choice ==1):
            print('*****************************RULES****************\n')
            print('The objective of the game is to get as close to 21 points as possible without going over. ')
            print('Each round, the two players take turns throwing two dies as many times as they like and adding up the totals.')
            print('A player who has a total of more than 21 is considered bust and loses the game.')
            print('After each player has taken a turn, the player with the closest total to 21 wins the game.\n')
        
        #user chooses to Play
        elif(main_choice ==2):

            #print cards
            print('-------------------------------------------------')
            print ("The dealer is showing a " + str(dealer_hand[0]))
            print ("You have a " + str(player_hand) + " for a total of " + str(total_in_hand(player_hand)))
            print('-------------------------------------------------')
            
            #check for Blackjack Conditon
            blackjack(dealer_hand, player_hand)

            #choose to get another card "hit" or not get another card "stand" or quit
            choice = input("1.Enter H or h for A hit.\n2.Enter S or s to Stand.\n3.Enter Q or q or 3 to Quit. ").lower()
            if choice == "h":
                hit(player_hand)
                while total_in_hand(dealer_hand) < 17:
                    hit(dealer_hand)
                score(dealer_hand, player_hand)
                play_again()
            elif(choice == "s"):
                while total_in_hand(dealer_hand) < 17:
                    hit(dealer_hand)
                score(dealer_hand, player_hand)
                play_again()
            elif choice == "q" or choice =='3':
                print ("Bye!")
                exit()
        #quit
        elif main_choice==3:
            print('Okay,Bye')
            exit()
	
if __name__ == "__main__":
    #call main
    game()
