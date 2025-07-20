# GUI version of Blackjack using pygame
import pygame
import random
import sys

# Game settings
WIDTH, HEIGHT = 800, 600
BG_COLOR = (34, 139, 34)  # green
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
FONT = pygame.font.SysFont(None, 32)
BIG_FONT = pygame.font.SysFont(None, 48)


def draw_text(surface, text, pos, font=FONT, color=WHITE):
    img = font.render(text, True, color)
    surface.blit(img, pos)


def check_winner(player_sum, dealer_sum, bet, chips):
    message = ""
    if player_sum == 21 and dealer_sum != 21:
        message = 'Blackjack! You win 1.5x your bet!'
        chips += int(bet * 1.5)
    elif dealer_sum == 21 and player_sum != 21:
        message = 'Dealer has blackjack. You lose your bet.'
        chips -= bet
    elif player_sum == 21 and dealer_sum == 21:
        message = 'Both you and dealer have blackjack. Push.'
    elif player_sum > 21:
        message = 'You bust! You lose your bet.'
        chips -= bet
    elif dealer_sum > 21:
        message = 'Dealer busts! You win your bet.'
        chips += bet
    elif player_sum > dealer_sum:
        message = 'You win!'
        chips += bet
    elif dealer_sum > player_sum:
        message = 'Dealer wins!'
        chips -= bet
    else:
        message = 'It is a push.'
    return message, chips


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Blackjack')

    chips = 2000
    clock = pygame.time.Clock()
    state = 'waiting'  # waiting -> betting -> playing -> result
    bet_input = ''
    bet = 0
    deck = []
    player_hand = []
    dealer_hand = []
    message = ''
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif state == 'waiting':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    state = 'betting'
            elif state == 'betting':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and bet_input:
                        bet = int(bet_input)
                        state = 'playing'
                        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4
                        random.shuffle(deck)
                        player_hand = [deck.pop(), deck.pop()]
                        dealer_hand = [deck.pop(), deck.pop()]
                    elif event.key == pygame.K_BACKSPACE:
                        bet_input = bet_input[:-1]
                    elif event.unicode.isdigit():
                        bet_input += event.unicode
            elif state == 'playing':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if 50 <= x <= 150 and 500 <= y <= 540:  # hit
                        player_hand.append(deck.pop())
                        if sum(player_hand) >= 21:
                            state = 'dealer'
                    if 200 <= x <= 300 and 500 <= y <= 540:  # stay
                        state = 'dealer'
            elif state == 'result':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if chips <= 0:
                        running = False
                    else:
                        state = 'betting'
                        bet_input = ''
        if state == 'waiting':
            draw_text(screen, f'Chips: {chips}', (50, 50), BIG_FONT)
            draw_text(screen, 'Press ENTER to start', (50, 100))
            draw_text(screen, f'Chips: {chips}', (50, 50), BIG_FONT)
            draw_text(screen, 'Press ENTER to start', (50, 100))
            if any(event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN for event in pygame.event.get()):
                state = 'betting'
        elif state == 'betting':
            draw_text(screen, f'Chips: {chips}', (50, 50), BIG_FONT)
            draw_text(screen, 'Enter bet and press ENTER:', (50, 150))
            draw_text(screen, bet_input, (50, 200), BIG_FONT)
        elif state in ('playing', 'dealer'):
            draw_text(screen, f'Bet: {bet}', (50, 50))
            draw_text(screen, f'Chips: {chips}', (200, 50))
            draw_text(
                screen, f'Your hand: {player_hand} = {sum(player_hand)}', (50, 150))
            draw_text(
                screen, f"Dealer's hand: {dealer_hand[0]} [?]", (50, 200))
            pygame.draw.rect(screen, BLACK, (50, 500, 100, 40))
            pygame.draw.rect(screen, BLACK, (200, 500, 100, 40))
            draw_text(screen, 'Hit', (75, 510))
            draw_text(screen, 'Stay', (220, 510))
            if state == 'dealer':
                while sum(dealer_hand) < 17 or (sum(dealer_hand) < sum(player_hand) and sum(dealer_hand) < 21):
                    dealer_hand.append(deck.pop())
                message, chips = check_winner(
                    sum(player_hand), sum(dealer_hand), bet, chips)
                state = 'result'
        elif state == 'result':
            draw_text(screen, message, (50, 150), BIG_FONT)
            draw_text(
                screen, f'Your hand: {player_hand} = {sum(player_hand)}', (50, 250))
            draw_text(
                screen, f"Dealer's hand: {dealer_hand} = {sum(dealer_hand)}", (50, 300))
            if chips > 0:
                draw_text(screen, 'Press ENTER to play again', (50, 400))
            else:
                draw_text(
                    screen, 'Out of chips! Press ENTER to quit.', (50, 400))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
