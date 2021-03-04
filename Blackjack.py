# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import os
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.balance = 1000

    def add_cards(self, new_cards):
        self.all_cards.append(new_cards)

    def sum_hand(self):
        return sum([x.value for x in self.all_cards])

    def ace_value(self):
        for x in self.all_cards:
            if x.rank == 'Ace':
                while True:
                    try:
                        x.rank = int(input("What is your desired Ace's rank? (1 or 11)"))
                        if x.rank not in [1, 11]:
                            raise TypeError
                        break
                    except TypeError:
                        print('Please return a proper value')

    def bet(self, amount):
        print(f'You bet {amount}$')
        self.balance -= amount
        self.bet_amount = amount

    def player_hand(self):
        print(f"{self.name}'s hand: {len(self.all_cards)}. {self.name} has {self.balance}$ left")
        print(*self.all_cards, sep='\n')

    def clear_hand(self):
        self.all_cards = []

    def __str__(self):
        return self.name


def new_game():
    global n, player_name, dealer
    player_name = []
    while True:
        try:
            n = int(input('Please enter the number of players:'))
            if n < 1:
                continue
            else:
                break
        except TypeError:
            print('You did not enter a number')
    for i in range(n):
        player_name.append(Player(input(f'Enter player {i+1} name:')))
    AIdealer = input('Do you want to have AI Dealer enabled?')
    while AIdealer.upper() not in ['Y', 'N']:
        AIdealer = input('Please re-enter. Are you an idiot?')
    if AIdealer.upper() == 'Y':
        dealer = Player('Dealer')
    else:
        dealer = random.choice(player_name)
        print(f'{dealer} will be the dealer!')
        player_name.remove(dealer)


def check_busted(player):
    print(player.sum_hand())
    if player.sum_hand() > 21:
        print(f"{player} busted!")
        return True
    return False


def check_lose(player):
    if player.balance <= 0:
        player_name.remove(player)


new_game()
while True:
    os.system('cls')
    deck = Deck()
    deck.shuffle()
    dealer.clear_hand()
    for i in player_name:
        i.clear_hand()
        while True:
            try:
                bet_amount = int(input(f'Player {i}, please enter your bet amount. Min step: 1$\nYou have {i.balance}$ left\n'))
                if i.balance < bet_amount or bet_amount < 1:
                    print('You cannot bet more than your balance, idiot.')
                    continue
                else:
                    i.bet(bet_amount)
                    break
            except TypeError or ValueError:
                print("For god's sake, please enter a proper amount.")
    for x in range(2):
        os.system('cls')
        for i in player_name:
            i.add_cards(deck.deal_one())
            i.player_hand()
            if i.sum_hand() == 21 and x == 1:
                print('Blackjack!')
                i.balance += 2.5*i.bet_amount
                dealer.balance -= i.bet_amount
        dealer.add_cards(deck.deal_one())
        print(f"{dealer}'s hand: {x+1}")
        print(f'{dealer.all_cards[0]}')
        if x == 1:
            print('Hidden Card')
    for x in player_name:
        print(f"{x}'s turn:")
        while True:
            add = input('Do you want to add more cards? [Y/ N]')
            while add.upper() not in ['Y', 'N']:
                add = input('Please enter the right answer at least one!')
            if add.upper() == 'Y':
                x.add_cards(deck.deal_one())
                print(x.all_cards[-1])
            else:
                x.ace_value()
                break
        check_busted(x)
    while True:
        dealer.player_hand()
        if dealer.sum_hand() == 21:
            print('Dealer has Blackjack')
        while dealer.sum_hand() < 17:
            dealer.add_cards(deck.deal_one())
        break
    if check_busted(dealer) is True:
        for x in player_name:
            dealer.balance -= x.bet_amount
            x.balance += 2*x.bet_amount
    for x in player_name:
        if x.sum_hand() > dealer.sum_hand():
            x.balance += 2*x.bet_amount
            dealer.balance -= x.bet_amount
        if x.sum_hand() == dealer.sum_hand():
            x.balance += x.bet_amount
        else:
            dealer.balance += x.balance
    for x in player_name:
        print(f"{x}'s balance: {x.balance}$ ")
        check_lose(x)
    continue_game = input('Do you want to continue or play a new game or quit? [C/N/Q]')
    while continue_game.upper() not in ['C', 'N', 'Q']:
        continue_game = input('Please re-enter.')
    if continue_game.upper() == 'Q':
        print('Goodbye')
        break
    elif continue_game.upper() == 'N':
        new_game()
