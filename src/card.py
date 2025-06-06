from tkinter import PhotoImage
from random import shuffle

VALUES = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]


class Card:
    """Takes string inputs of a value and suit and generates a card object with a matching image and point value"""

    def __init__(self, value, suit):
        # Value and suit are saved seperately for ease of generation later.
        self.value = value
        self.suit = suit
        self.img_path = f"./static/{suit.lower()}_{value.title()}.png"
        self.img = PhotoImage(file=self.img_path)
        if self.value == "jack" or self.value == "queen" or self.value == "king":
            self.points = 10
        elif self.value == "ace":
            self.points = 1
        else:
            self.points = int(self.value)
        self.counter = False


class Deck:
    """Creates a deck of 52 cards and shuffles it."""

    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for value in VALUES:
                self.deck.append(Card(value, suit))
        shuffle(self.deck)

    def deal(self, player):
        """Takes a player object as input and appends the topmost card of the deck to their hand."""
        player.hand.append(self.deck.pop())
