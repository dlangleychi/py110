'''
1. Initialize deck
    suits don't matter, four of each card in list
2. Deal cards to player and dealer
    randomize cards, player and dealer hands are lists
    print holdings
3. Player turn: hit or stay
   - repeat until bust or stay
    while true loop, break if bust or stay
4. If player bust, dealer wins.
    if condition
5. Dealer turn: hit or stay
   - repeat until total >= 17
   while true loop for dealer
6. If dealer busts, player wins.
    if condition
7. Compare cards and declare winner.
    if condition for winner
'''

import random

CARDS = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 
    'Jack', 'Queen', 'King', 'Ace'
]

NUMBER_SUITS = 4

SCORE_LIMIT = 21

DEALER_STAY = 17

def make_deck():
    """
    Make and return a shuffled deck.
    """
    deck = []
    for card in CARDS:
        deck.extend([card] * NUMBER_SUITS)
    random.shuffle(deck)
    return deck

def score_hand(hand):
    """
    Calculate the value of a hand.
    """
    score = 0
    aces = 0
    for card in hand:
        if card == CARDS[12]:
            score += 11
            aces += 1
        elif card in CARDS[9:12]:
            score += 10
        else:
            score += int(card)

    while score > SCORE_LIMIT and aces:
        score -= 10
        aces -= 1

    return score

def deal(deck, hand):
    """
    Deal card into hand.
    """
    hand.append(deck.pop())

def display_hand(hand, name):
    """
    Print cards in hand and hand score.
    """
    print(f"\n{name} hand: {', '.join(hand)}")
    print(f'Score is {score_hand(hand)}')

def play_game():
    """
    Play a game of twenty one.
    """
    # make deck and shuffle
    deck = make_deck()

    # deal and show cards
    player_hand = []
    dealer_hand = []

    deal(deck, player_hand)
    deal(deck, dealer_hand)
    deal(deck, player_hand)
    deal(deck, dealer_hand)

    print(f'Dealer has: {dealer_hand[0]} and unknown card')
    print(f'You have: {player_hand[0]} and {player_hand[1]}')

    # player turn
    player_score = score_hand(player_hand)
    while True:
        # print(f'\nYour hand is: {", ".join(player_hand)}.')
        # print(f'You have {player_score}.')
        display_hand(player_hand, 'Your')
        answer = input('hit of stay? ')
        if answer == 'hit':
            deal(deck, player_hand)
            player_score = score_hand(player_hand)
            if player_score > SCORE_LIMIT:
                break
        elif answer == 'stay':
            break
        else:
            print('Invalid input.  Please try again.')

    # did player bust?
    if player_score > SCORE_LIMIT:
        display_hand(player_hand, 'Your')
        print('Player busted.  Dealer wins.')
        return

    # dealers turn
    dealer_score = score_hand(dealer_hand)
    while dealer_score < DEALER_STAY:
        display_hand(dealer_hand, 'Dealer')
        print('Dealer hits.')
        deal(deck, dealer_hand)

        dealer_score = score_hand(dealer_hand)

    # did dealer bust?
    if dealer_score > SCORE_LIMIT:
        display_hand(dealer_hand, 'Dealer')
        print('Dealer busted.  Player wins.')
        return

    # determine winner
    display_hand(dealer_hand, 'Dealer')

    print(f'Player score: {player_score}; Dealer score: {dealer_score}')
    if player_score > dealer_score:
        print('Player wins!')
    elif player_score < dealer_score:
        print('Dealer wins!')
    else:
        print('Tie!')

play_game()
