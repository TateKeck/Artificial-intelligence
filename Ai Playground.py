# Programmer: Tate Keck
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI technology ")

import random
from enum import Enum

class Rank(Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'

class Suit(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank.value} of {self.suit.value}"

def create_deck():
    ranks = list(Rank)
    suits = list(Suit)
    deck = [Card(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def get_card_value(card):
    if card.rank in [Rank.JACK, Rank.QUEEN, Rank.KING]:
        return 10
    elif card.rank == Rank.ACE:
        return 11
    else:
        return int(card.rank.value)

def calculate_hand_value(hand):
    value = sum(get_card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card.rank == Rank.ACE)
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value

def print_hand(hand):
    for card in hand:
        print(card)

def blackjack():
    print("Welcome to Blackjack!")
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Dealer's Hand:")
    print(dealer_hand[0])
    print("Player's Hand:")
    print_hand(player_hand)

    player_value = calculate_hand_value(player_hand)
    while player_value < 21:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            print("Player's Hand:")
            print_hand(player_hand)
            player_value = calculate_hand_value(player_hand)
        elif action == 's':
            break
        else:
            print("Invalid input! Please enter 'h' or 's'.")

    if player_value > 21:
        print("You busted! Dealer wins.")
        return

    print("Dealer's Hand:")
    print_hand(dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print("Dealer draws a card...")
        print_hand(dealer_hand)

    dealer_value = calculate_hand_value(dealer_hand)
    if dealer_value > 21:
        print("Dealer busted! You win.")
    elif dealer_value > player_value:
        print("Dealer wins.")
    elif dealer_value < player_value:
        print("You win!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    blackjack()
