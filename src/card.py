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
        # Image path generation
        self.img_path = f"./static/{suit.lower()}_{value.title()}.png"
        self.img = PhotoImage(file=self.img_path)
        # Attributes for functions to track if a card has been operated on.
        self.counted = False
        # How many points each card is worth.
        if self.value == "Jack" or self.value == "Queen" or self.value == "King":
            self.points = 10
        elif self.value == "Ace":
            self.points = 11
        else:
            self.points = int(self.value)


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
        if not player.bust and not player.stand:
            player.hand.append(self.deck.pop())
            player.calculate_score()
            player.display_cards()

    def reset(self, player, player2):
        """Resets the deck."""
        # Unmark all of our drawn cards and dump them back into the deck, then shuffle.
        for card in player.hand:
            card.counted = False
            if card.value == "Ace":
                card.points = 11
        for card in player2.hand:
            card.counted = False
            if card.value == "Ace":
                card.points = 11
        self.deck.extend(player.hand)
        self.deck.extend(player2.hand)
        shuffle(self.deck)
