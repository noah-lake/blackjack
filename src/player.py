from tkinter import Label


class Player:
    def __init__(self, side, window):
        self.hand = []
        self.score = 0
        self.bust = False
        self.stand = False
        self.side = side
        self.active = False
        self.ready = False
        self.window = window
        self.score_label = Label(
            window.root,
            text="Score",
            anchor="center",
            width=8,
            bg="black",
            fg="white",
        )

    def calculate_score(self):
        """Updates the player's score, then checks if the player's score is exactly 21 or if their score is over 21."""
        for card in self.hand:
            if not card.counted:
                card.counted = True
                self.score += card.points
        self.score_label.configure(text=f"{self.score}")
        # Perfect score detection
        if self.score == 21:
            if len(self.hand) <= 2:
                self.score_label.configure(text="Blackjack!")
            self.stand = True
        # Ace revaluing
        self.ace_check()
        # If total is still greater than 21 after ace revaluing, player is bust. Set their score to zero.
        if self.score > 21:
            self.bust = True
            self.score = 0
            self.score_label.configure(text="Bust")

    def ace_check(self):
        """Checks if the player's score is over 21, then iterates through their hand, revaluing any
        aces one at a time until their score is less than 21 or until no aces are found."""
        # If the score is less than 21, then the Ace is fine as an 11.
        if self.score > 21:
            operations = 0
            for card in self.hand:
                # If a card is an ace had has a point value of 11 (meaning it has not been modified)
                if card.value == "Ace" and card.points == 11:
                    # Track that we've changed something
                    operations += 1
                    # Change the card value.
                    # We could technically set this value to antyhing. The card isn't going to be counted again.
                    card.points = 1
                    # Reduce the score by 10.
                    self.score -= 10
                    # Update the score label.
                    self.score_label.configure(text=f"{self.score}")
                    # Break out. We want to check only one ace at a time.
                    break
            # If the score is still greater than 21 and we've done an operation already, ace check again.
            if self.score > 21 and operations > 1:
                self.ace_check()

    def display_cards(self):
        """Adds the card images to the screen, keeping the stack centered on that player's side of the screen.
        Each successive card is offset by 50 pixels."""
        # If this is the left side player (player one), set their cards in the middle of the left half of the
        # sceen. Offset the first card to the left by 25 pixels for each card in hand beyond the fist.
        if self.side == "left":
            x = (
                self.window.width // 2
                - self.window.width // 4
                - (25 * (len(self.hand) - 1))
            )
        # If this is the rigth side player (player two), set thier cards in the middle of the right half of the
        # screen. Offset the first card to the left by 25 pixels for each card in hand beyond the first.
        else:
            x = (
                self.window.width // 2
                + self.window.width // 4
                - (25 * (len(self.hand) - 1))
            )
        # Add the images to the screen. Create each card fifty pixels further to the right than the last.
        for card in self.hand:
            self.window.canvas.create_image(x, 400, image=card.img)
            x += 50

    def set_ready(self):
        """Helper function for use in a button"""
        self.ready = True

    def make_active(self):
        """Helper function for use in a button"""
        self.active = True

    def set_stand(self):
        """Helper function for use in a button."""
        self.stand = True

    def reset(self):
        """Resets the player's attributes to their base values."""
        self.hand.clear()
        self.score = 0
        self.score_label.configure(text=f"{self.score}")
        self.active = False
        self.ready = False
        self.stand = False
        self.bust = False
