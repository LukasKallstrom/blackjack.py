import random
import time
chips = 2000
lose_count = 0

def lose_chips(bet):
    global chips
    chips = chips - bet
    print("Your have lost", bet, "chips and have", chips, "chips left.")

def win_chips(bet):
    global chips
    chips = chips + bet
    print("You have won", bet, "chips and have", chips, "chips left.")

while 1:
    """
    Play a game of blackjack
    """
    print("-------------------------")
    # create a deck of cards
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

    # shuffle the deck
    random.shuffle(deck)

    # create a player and dealer hands
    player_hand = []
    dealer_hand = []

    # show the player their chips
    if chips > 0:
        print("You have", chips, "chips.")
    elif lose_count == 0:
        chips = 1
        print("You have no chips left. But we pitty you so here, take a chip. (+1 chip)")
        print("You have", chips, "chips.")
    else:
        print("You have no chips left. You lose.")
        time.sleep(4)
        break

    # the player bets chips
    while True:
        try:
            bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, please enter a number.")
        else:
            if bet > chips:
                print("Sorry, you don't have enough chips.")
            else:
                break
    
    # deal two cards to each player
    player_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    # show the player's hand
    print('Your hand: {} = {}'.format(player_hand, sum(player_hand)))

    # show the dealer's hand
    print('Dealer\'s hand: {} = {}'.format(dealer_hand, sum(dealer_hand)))

    # ask the player if they want to hit or stay
    hit_or_stay = input('Would you like to hit or stay? ')

    # if the player hits, add a card to their hand
    # let the player hit several times until they stay or bust

    while (hit_or_stay == 'hit') & (sum(player_hand) <= 21):
        time.sleep(1)
        player_hand.append(deck.pop())
        print('Your hand: {} = {}'.format(player_hand, sum(player_hand)))
        hit_or_stay = input('Would you like to hit or stay?: ')

    # if the player stays, the dealer plays
    while sum(dealer_hand) < 17:
        time.sleep(1)
        dealer_hand.append(deck.pop())
        print('Dealer hits: {} = {}'.format(dealer_hand, sum(dealer_hand)))
            
    # show your final hand
    time.sleep(1)
    print('\nYour final hand: {} = {}'.format(player_hand, sum(player_hand)))

    # show the dealer's final hand
    time.sleep(1)
    print('Dealer\'s final hand: {} = {}\n'.format(dealer_hand, sum(dealer_hand)))

    # determine the winner
    if (sum(player_hand) > sum(dealer_hand)):
        if (sum(player_hand) == 21):
            print('Blackjack! You win!')
            win_chips(bet*2)
        elif (sum(player_hand)) <= 21:
            print('You win!')
            win_chips(bet)
        elif (sum(player_hand) > 21) & (sum(dealer_hand) <= 21): 
            print('You lose!')
            lose_chips(bet)
    elif (sum(dealer_hand) > sum(player_hand)):
        if (sum(dealer_hand) <= 21):
            print('Dealer wins!')
            lose_chips(bet)
        elif (sum(dealer_hand) > 21) & (sum(player_hand) <= 21):
            print('You win!')
            win_chips(bet)
    else:
        print('You push!')

    # ask if the player wants to play again
    play_again = input('Would you like to play again? ')

    # if the player wants to play again, restart the game
    if play_again == 'yes':
        print('-------------------------\n')

    # if the player does not want to play again, exit the game
    else:
        print('Thanks for playing!')
        exit()
