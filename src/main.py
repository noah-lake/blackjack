from tkinter import HIDDEN, Button
from graphics import Window
from card import Deck
from player import Player


def check_winner(win, player, player2):
    """Determines the winner of the game and displays it on screen."""
    if player.bust and player2.bust:
        win.canvas.create_text(
            win.width // 2, 100, text="DRAW", anchor="center", font="Calibri 30 bold"
        )
    elif player.score == player2.score:
        win.canvas.create_text(
            win.width // 2, 100, text="DRAW", anchor="center", font="Calibri 30 bold"
        )
    elif player.bust and not player2.bust:
        win.canvas.create_text(
            win.width // 2,
            100,
            text="PLAYER 2 WINS",
            anchor="center",
            font="Calibri 30 bold",
        )
    elif player2.bust and not player.bust:
        win.canvas.create_text(
            win.width // 2,
            100,
            text="PLAYER 1 WINS",
            anchor="center",
            font="Calibri 30 bold",
        )
    elif player.score > player2.score:
        win.canvas.create_text(
            win.width // 2,
            100,
            text="PLAYER 1 WINS",
            anchor="center",
            font="Calibri 30 bold",
        )
    else:
        win.canvas.create_text(
            win.width // 2,
            100,
            text="PLAYER 2 WINS",
            anchor="center",
            font="Calibri 30 bold",
        )


def main_menu(win, player, player2):
    """Shows the title screen with player number select buttons."""
    win.running = True
    title = win.canvas.create_text(
        win.width // 2,
        200,
        text="B L A C K J A C K",
        anchor="center",
        font="Calibri 50 bold",
    )
    player_select = win.canvas.create_text(
        win.width // 2,
        450,
        text="Select number of players",
        anchor="center",
        font="Calibri 20 bold",
    )
    one_player = Button(
        win.root,
        text="Singleplayer",
        command=lambda: [win.start_game(deck, player, player2), hide_menu()],
        width=12,
        bg="black",
        fg="white",
    )
    versus = Button(
        win.root,
        text="Versus",
        command=lambda: [
            hide_menu(),
            player2.make_active(),
            win.start_game(deck, player, player2),
        ],
        width=12,
        bg="black",
        fg="white",
    )
    one_player.place(x=win.width // 2 - 225, y=500)
    versus.place(x=win.width // 2 + 75, y=500)

    def hide_menu():
        """Hides the main menu items."""
        win.canvas.itemconfigure(title, state=HIDDEN)
        win.canvas.itemconfigure(player_select, state=HIDDEN)
        one_player.destroy()
        versus.destroy()


win = Window(1700, 640)
player = Player("left", win)
player2 = Player("right", win)
deck = Deck()
main_menu(win, player, player2)

while win.running:
    win.root.update()
    win.root.update_idletasks()
    if not player2.active and player2.ready:
        if player2.score < 17:
            deck.deal(player2)
            if not player.stand and not player.bust:
                player2.ready = False
        else:
            player2.set_stand()

    if (player.stand or player.bust) and (player2.stand or player2.bust):
        check_winner(win, player, player2)
