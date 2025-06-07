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
        # If total is still greater than 21 after ace revaluing, player is bust.
        if self.score > 21:
            self.bust = True
            self.score_label.configure(text="Bust")

    def ace_check(self):
        """Checks if the player's score is over 21, then iterates through their hand, revaluing any
        aces one at a time until their score is less than 21 or until no aces are found."""
        if self.score > 21:
            operations = 0
            for card in self.hand:
                if card.value == "Ace" and card.points == 11:
                    operations += 1
                    # We could technically set this value to antyhing. The card isn't going to be counted again.
                    card.points = 1
                    self.score -= 10
                    self.score_label.configure(text=f"{self.score}")
                    break
            if self.score > 21 and operations > 1:
                self.ace_check()

    def display_cards(self):
        """Adds the card images to the screen, keeping the stack centered on that player's side of the screen.
        Each successive card is offset by 50 pixels."""
        if self.side == "left":
            x = (
                self.window.width // 2
                - self.window.width // 4
                - (25 * (len(self.hand) - 1))
            )
        else:
            x = (
                self.window.width // 2
                + self.window.width // 4
                - (25 * (len(self.hand) - 1))
            )
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
        self.hand.clear()
        self.score = 0
        self.score_label.configure(text=f"{self.score}")
        self.active = False
        self.ready = False
        self.stand = False
        self.bust = False
