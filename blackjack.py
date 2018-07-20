import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',
    'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The Deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        if card.rank == 'Ace':
            self.aces += 1
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_aces(self):
        if self.value >= 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please place your bet: '))
        except ValueError:
            print('Bet must be integer')
        else:
            if chips.bet > chips.total:
                print(f'You can bet a max. of {chips.total}')
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()


def hit_or_stand(deck, hand):
    global playing
    choise = input("Want to hit (h) or stand (s)? ")
    if choise == "hit" or choise == "h":
        hit(deck, hand)
    elif choise == "stand" or choise == "s":
        playing = False


def show_some(player, dealer):
    print('\nDealers Hand:')
    print('<Card hidden>')
    print(' ', dealer.cards[1])
    print('\nPlayers Cards:', *player.cards, sep='\n ')


def show_all(player, dealer):
    print('\nDealers Cards:', *dealer.cards, sep='\n ')
    print('Dealers Hand = ', dealer.value)
    print('\nPlayers Cards:', *player.cards, sep='\n ')
    print('Players Hand = ', player.value)


def player_busts(chips):
    print('Player busts!')
    chips.lose_bet()


def player_wins(chips):
    print('Player wins!')
    chips.win_bet()


def dealer_busts(chips):
    print('Dealer busts!')
    chips.win_bet()


def dealer_wins(chips):
    print('Dealer wins!')
    chips.lose_bet()


def tie():
    print('Tie!')


while True:

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            tie()

    print("\nPlayer's winnings stand at", player_chips.total)
    new_game = input('Play again? y/n')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break
