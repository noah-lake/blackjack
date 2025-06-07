from tkinter import Tk, Canvas, PhotoImage, Button, HIDDEN


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
                command=player2.set_stand,
                anchor="center",
                font=("Arial", 12),
                width=5,
                bg="black",
                fg="white",
            )
            # ... and add them to the screen.
            player_two_hit.place(x=self.width // 2 + self.width // 4 - 75, y=100)
            player_two_stand.place(x=self.width // 2 + self.width // 4 + 5, y=100)

    def main_menu(self, deck, player, player2):
        """Shows the title screen with player number select buttons."""
        # Start the logic loop
        self.running = True
        # Create the title
        title = self.canvas.create_text(
            self.width // 2,
            200,
            text="B L A C K J A C K",
            anchor="center",
            font="Calibri 50 bold",
        )
        # Create the player select text and buttons
        player_select = self.canvas.create_text(
            self.width // 2,
            450,
            text="Select number of players",
            anchor="center",
            font="Calibri 20 bold",
        )

        one_player = Button(
            self.root,
            text="Singleplayer",
            # Singleplayer mode calls the start_game and hides the menu elements. It's the "default"
            command=lambda: [self.start_game(deck, player, player2), hide_menu()],
            width=12,
            bg="black",
            fg="white",
        )

        versus = Button(
            self.root,
            text="Versus",
            # Versus mode marks player two as active, disabling the logic loop that would control them.
            # It is otherwise identical to singleplayer.
            command=lambda: [
                hide_menu(),
                player2.make_active(),
                self.start_game(deck, player, player2),
            ],
            width=12,
            bg="black",
            fg="white",
        )
        # Display buttons
        one_player.place(x=self.width // 2 - 225, y=500)
        versus.place(x=self.width // 2 + 75, y=500)

        # Helper function to hide or destroy menu elements when the game starts.
        def hide_menu():
            """Hides the main menu items."""
            self.canvas.itemconfigure(title, state=HIDDEN)
            self.canvas.itemconfigure(player_select, state=HIDDEN)
            one_player.destroy()
            versus.destroy()

    def reset(self, player, player2):
        """Clears the screen of widgets and images except for the base background."""
        # Delete all of the children of root except canvas and the score labels.
        for widget in self.root.winfo_children():
            if (
                widget != self.canvas
                and widget != player.score_label
                and widget != player2.score_label
            ):
                widget.destroy()
        # Hide the score labels
        player.score_label.place_forget()
        player2.score_label.place_forget()
        # Wipe the canvas
        self.canvas.delete("all")
        # Rebuild the background images
        self.generate_background()
