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

class Blackjack:
    def __init__(self):
        self.player_chips = 100
        self.deck = self.create_deck()

    def create_deck(self):
        ranks = list(Rank)
        suits = list(Suit)
        deck = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def get_card_value(self, card):
        if card.rank in [Rank.JACK, Rank.QUEEN, Rank.KING]:
            return 10
        elif card.rank == Rank.ACE:
            return 11
        else:
            return int(card.rank.value)

    def calculate_hand_value(self, hand):
        value = sum(self.get_card_value(card) for card in hand)
        num_aces = sum(1 for card in hand if card.rank == Rank.ACE)
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value

    def print_hand(self, hand):
        for card in hand:
            print(card)

    def place_bet(self):
        while True:
            try:
                bet = int(input(f"Place your bet (you have {self.player_chips} chips): "))
                if bet < 1 or bet > self.player_chips:
                    raise ValueError
                break
            except ValueError:
                print("Invalid bet amount. Please enter a valid number.")

        return bet

    def play_round(self):
        print("\nWelcome to Blackjack!")
        bet = self.place_bet()

        player_hand = [self.deck.pop(), self.deck.pop()]
        dealer_hand = [self.deck.pop(), self.deck.pop()]

        print("\nDealer's Hand:")
        print(dealer_hand[0])
        print("\nPlayer's Hand:")
        self.print_hand(player_hand)

        if self.calculate_hand_value(player_hand) == 21:
            print("Blackjack! You win!")
            self.player_chips += 1.5 * bet
            return

        while True:
            action = input("Do you want to hit, stand, double down, or split? (h/s/d/p): ").lower()
            if action == 'h':
                player_hand.append(self.deck.pop())
                print("\nPlayer's Hand:")
                self.print_hand(player_hand)
                if self.calculate_hand_value(player_hand) > 21:
                    print("You busted! Dealer wins.")
                    self.player_chips -= bet
                    return
            elif action == 's':
                break
            elif action == 'd':
                bet *= 2
                player_hand.append(self.deck.pop())
                print("\nPlayer's Hand:")
                self.print_hand(player_hand)
                if self.calculate_hand_value(player_hand) > 21:
                    print("You busted! Dealer wins.")
                    self.player_chips -= bet
                    return
                break
            elif action == 'p':
                print("Splitting is not implemented yet. Please choose another action.")
            else:
                print("Invalid input! Please enter 'h', 's', 'd', or 'p'.")

        print("\nDealer's Hand:")
        self.print_hand(dealer_hand)
        while self.calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(self.deck.pop())
            print("Dealer draws a card...")
            self.print_hand(dealer_hand)

        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        if dealer_value > 21:
            print("Dealer busted! You win!")
            self.player_chips += bet
        elif dealer_value > player_value:
            print("Dealer wins.")
            self.player_chips -= bet
        elif dealer_value < player_value:
            print("You win!")
            self.player_chips += bet
        else:
            print("It's a tie!")

    def play(self):
        while self.player_chips > 0:
            self.play_round()
            if input("\nDo you want to play another round? (y/n): ").lower() != 'y':
                break
        print(f"\nYou finished the game with {self.player_chips} chips. Thanks for playing!")

if __name__ == "__main__":
    game = Blackjack()
    game.play()
