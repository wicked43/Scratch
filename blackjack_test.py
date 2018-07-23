import random

numbers = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

game_round = True


class Card:
    def __init__(self, number):
        self.number = number
        self.value = values.get(self.number)

    def __str__(self):
        return self.number


class Deck:
    def __init__(self):
        self.deck = []
        for color in range(4):
            for number in numbers:
                self.deck.append(Card(number))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return 'Deck: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return str(self.cards)

    def add_card(self, card):
        if card.number == 'A':
            self.aces += 1
        self.value += card.value
        self.cards.append(card)

    def adjust_for_aces(self):
        if self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.stack = 100
        self.bet = 0

    def win_bet(self):
        self.stack += self.bet

    def lose_bet(self):
        self.stack -= self.bet


def place_bet(chips):
    while True:
        bet = int(input(f'Place your bet! (max. {chips.stack}'))
        if bet > chips.stack:
            print('You do not have enough Chips!')
        else:
            chips.bet = bet
            break


def player_bust(chips):
    print('You bust!')
    chips.lose_bet()


def player_wins(chips):
    print('You win!')
    chips.win_bet()


def dealer_bust(chips):
    print('Dealer busts!')
    chips.win_bet()


def dealer_wins(chips):
    print('Dealer wins!')
    chips.lose_bet()


def tie():
    print('Tie!')


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()


def show_some(player_hand, dealer_hand):
    print('Dealer: \n')
    print(' <card hidden> \n', dealer_hand.cards[1], '\n')
    print('\nPlayer:', *player_hand.cards, sep='\n ')


def show_all(player_hand, dealer_hand):
    print('\nDealer:', *dealer_hand.cards, sep='\n ')
    print('Dealer Value =', dealer_hand.value)
    print('\nPlayer:', *player_hand.cards, sep='\n ')
    print('Player Value =', player_hand.value)


def hit_or_stay(hand, deck):
    global game_round
    choise = input("Want to hit (h) or stand (s)? ")
    if choise == "hit" or choise == "h":
        hit(deck, hand)
    elif choise == "stand" or choise == "s":
        game_round = False


# Game
chips = Chips()

while True:

    if chips.stack < 1:
        print('Sorry, you dont have any chips left!')
        break

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    # place bet
    place_bet(chips)

    # each player gets 2 cards
    hit(deck, player_hand)
    hit(deck, player_hand)

    hit(deck, dealer_hand)
    hit(deck, dealer_hand)

    show_some(player_hand, dealer_hand)

    while game_round:

        show_some(player_hand, dealer_hand)
        hit_or_stay(player_hand, deck)

        if player_hand.value > 21:
            player_bust(chips)
            show_all(player_hand, dealer_hand)
            game_round = False

    if player_hand.value < 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(chips)

        elif dealer_hand.value == 21:
            dealer_wins(chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(chips)

        elif player_hand.value > dealer_hand.value:
            player_wins(chips)

        else:
            tie()

    print("\nPlayer's winnings stand at", chips.stack)
    new_game = input('Play again? y/n')

    if new_game[0].lower() == 'y':
        game_round = True
        continue
    else:
        print('Thanks for playing!')
        break
