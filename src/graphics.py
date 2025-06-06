from tkinter import Tk, Canvas, PhotoImage, Button


class Window:
    """Takes integer height and width inputs to create a standard Tkinter window with a table
    as the background."""

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.title("Blackjack")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.table = PhotoImage(file="./static/table.png")
        self.line = PhotoImage(file="./static/line.png")
        self.generate_background()

    def close(self):
        self.running = False

    def generate_background(self):
        """Draws the background images onto the screen."""
        self.canvas.create_image(self.width // 2, self.height // 2, image=self.table)
        self.canvas.create_image(self.width // 2, self.height // 2, image=self.line)

    def start_game(self, deck, player, player2):
        """Sets up the score labels, stand and hit buttons for each human player, and deals out a card to each
        player."""
        # Score labels were created for each player at initialization, but are only placed onto the screen now.
        player.score_label.place(x=self.width // 2 - self.width // 4 - 35, y=50)
        player2.score_label.place(x=self.width // 2 + self.width // 4 - 35, y=50)

        # Deal a card to each player
        deck.deal(player)
        deck.deal(player2)

        # Button for player one to get another card.
        player_one_hit = Button(
            self.root,
            text="Hit",
            # Deal a card to player, but also set player two as "ready" for computer opponents.
            # No effect in versus mode.
            command=lambda: [deck.deal(player), player2.set_ready()],
            anchor=("center"),
            font=("Arial", 12),
            width=5,
            bg="black",
            fg="white",
        )
        # Button for player one to stop drawing cards.
        player_one_stand = Button(
            self.root,
            text="Stand",
            # Also sets player two as ready.
            command=lambda: [player.set_stand(), player2.set_ready()],
            anchor=("center"),
            font=("Arial", 12),
            width=5,
            bg="black",
            fg="white",
        )

        # Place the buttons on their respective sides of the screen
        player_one_hit.place(x=self.width // 2 - self.width // 4 - 75, y=100)
        player_one_stand.place(x=self.width // 2 - self.width // 4 + 5, y=100)

        # If player two is a human, create their buttons.
        if player2.active:
            player_two_hit = Button(
                self.root,
                text="Hit",
                command=lambda: deck.deal(player2),
                anchor=("center"),
                font=("Arial", 12),
                width=5,
                bg="black",
                fg="white",
            )
            player_two_stand = Button(
                self.root,
                text="Stand",
                command=player.set_stand,
                anchor="center",
                font=("Arial", 12),
                width=5,
                bg="black",
                fg="white",
            )
            # ... and add them to the screen.
            player_two_hit.place(x=self.width // 2 + self.width // 4 - 75, y=100)
            player_two_stand.place(x=self.width // 2 + self.width // 4 + 5, y=100)
