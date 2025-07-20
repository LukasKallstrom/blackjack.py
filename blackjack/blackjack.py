import random
import time
chips = 2000
lose_count = 0
double_down = False


def lose_chips(bet):
    global chips
    chips = chips - bet
    print("Your have lost", bet, "chips and have", chips, "chips left.")


def win_chips(bet):
    global chips
    chips = chips + bet
    print("You have won", bet, "chips and have", chips, "chips left.")


def check_winner(player_sum, dealer_sum, bet):
    # check for blackjack
    if player_sum == 21 and dealer_sum != 21:
        print('Blackjack! You win 1.5x your bet!')
        win_chips(int(bet * 1.5))
    elif dealer_sum == 21 and player_sum != 21:
        print('Dealer has blackjack. You lose your bet.')
        lose_chips(bet)
    elif player_sum == 21 and dealer_sum == 21:
        print('Both you and dealer have blackjack. It is a push.')
        # No chips won or lost in a push

    # check for bust
    elif player_sum > 21:
        print('You bust! You lose your bet.')
        lose_chips(bet)
    elif dealer_sum > 21:
        print('Dealer busts! You win your bet.')
        win_chips(bet)

    # normal play
    elif player_sum > dealer_sum:
        print('You win!')
        win_chips(bet)
    elif dealer_sum > player_sum:
        print('Dealer wins!')
        lose_chips(bet)
    elif dealer_sum == player_sum:
        print('It is a push.')
        # No chips won or lost in a push


def main():
    global chips
    while 1:
        print("\033c")
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
            print(
                "You have no chips left. But we pitty you so here, take a chip. (+1 chip)")
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
        for i in range(4):
            if i % 2 == 0:
                player_hand.append(deck.pop())
            else:
                dealer_hand.append(deck.pop())

        # show the player's hand
        print('Your hand: {} = {}'.format(player_hand, sum(player_hand)))

        # show the dealer's hand (only show the first card)
        print('Dealer\'s hand: [{}][?]'.format(dealer_hand[0]))
        # print('Dealer\'s hand: {} = {}'.format(dealer_hand, sum(dealer_hand)))

        # ask the player if they want to hit or stay
        if sum(player_hand) <= 21:
            hit_or_stay = input(
                'Would you like to hit, stay or double down? (hit/stay/double): ')
        else:
            hit_or_stay = 'stay'
        # if the player hits, add a card to their hand
        # let the player hit several times until they stay or bust
        if hit_or_stay == 'double':
            player_hand.append(deck.pop())
            print('Your hand: {} = {}'.format(player_hand, sum(player_hand)))
            hit_or_stay = 'stay'
            bet = bet * 2
        while (hit_or_stay == 'hit') & (sum(player_hand) <= 21):
            time.sleep(1)
            player_hand.append(deck.pop())
            print('Your hand: {} = {}'.format(player_hand, sum(player_hand)))
            hit_or_stay = input('Would you like to hit or stay?: ')

        # show the dealer's hand (all cards)
        print('Dealer\'s hand: {} = {}'.format(dealer_hand, sum(dealer_hand)))

        # if the player stays, the dealer plays
        while sum(dealer_hand) < 17 or (sum(dealer_hand) < sum(player_hand) and sum(dealer_hand) < 21):
            dealer_hand.append(deck.pop())
            print('Dealer hits: {} = {}'.format(dealer_hand, sum(dealer_hand)))

        # show your final hand
        time.sleep(1)
        print('-------------------------')
        print('Your final hand: {} = {}'.format(player_hand, sum(player_hand)))

        # show the dealer's final hand
        time.sleep(0.2)
        print('Dealer\'s final hand: {} = {}'.format(
            dealer_hand, sum(dealer_hand)))
        print('-------------------------')
        time.sleep(1)

        # determine the winner
        check_winner(sum(player_hand), sum(dealer_hand), bet)

        # ask if the player wants to play again
        play_again = input('Would you like to play again? (yes/no)')

        # if the player wants to play again, restart the game
        if play_again == 'yes':
            print('-------------------------\n')

        # if the player does not want to play again, exit the game
        else:
            print('Thanks for playing!')
            exit()


if __name__ == "__main__":
    main()
