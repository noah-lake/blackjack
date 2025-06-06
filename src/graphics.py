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
        self.__running = False
        self.table = PhotoImage(file="./static/table.png")
        self.line = PhotoImage(file="./static/line.png")
        self.generate_background()

    def close(self):
        self.__running = False

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.root.update()
            self.root.update_idletasks()

    def generate_background(self):
        self.canvas.create_image(self.width // 2, self.height // 2, image=self.table)
        self.canvas.create_image(self.width // 2, self.height // 2, image=self.line)

    def start_game(self, deck, player, player2):
        player.score_label.place(x=self.width // 2 - self.width // 4 - 35, y=50)
        player2.score_label.place(x=self.width // 2 + self.width // 4 - 35, y=50)

        deck.deal(player)
        deck.deal(player2)

        player_one_hit = Button(
            self.root,
            text="Hit",
            command=lambda: deck.deal(player),
            anchor=("center"),
            font=("Arial", 12),
            width=5,
            bg="black",
            fg="white",
        )
        player_one_stand = Button(
            self.root,
            text="Stand",
            command=player.set_stand,
            anchor=("center"),
            font=("Arial", 12),
            width=5,
            bg="black",
            fg="white",
        )

        player_one_hit.place(x=self.width // 2 - self.width // 4 - 75, y=100)
        player_one_stand.place(x=self.width // 2 - self.width // 4 + 5, y=100)
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

            player_two_hit.place(x=self.width // 2 + self.width // 4 - 75, y=100)
            player_two_stand.place(x=self.width // 2 + self.width // 4 + 5, y=100)
