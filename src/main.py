from tkinter import Button
from graphics import Window
from card import Deck
from player import Player
from time import sleep


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


def pre_reset(win, player, player2):
    reset_button = Button(
        win.root,
        text="Reset",
        command=lambda: [
            reset(),
            reset_button.destroy(),
            win.main_menu(deck, player, player2),
        ],
        width=5,
        bg="black",
        fg="white",
    )
    # Set player one's stand and bust attributes to ensure that the while loop does not
    # continually place reset buttons.
    player.stand = False
    player.bust = False
    reset_button.place(x=win.width // 2 - 40, y=600)


def reset():
    win.reset(player, player2)
    deck.reset(player, player2)
    player.reset()
    player2.reset()


win = Window(1700, 640)
player = Player("left", win)
player2 = Player("right", win)
deck = Deck()


def main():
    win.main_menu(deck, player, player2)

    while win.running:
        win.root.update()
        win.root.update_idletasks()
        if not player2.active and player2.ready and not player.bust:
            if player2.score < 17:
                sleep(0.5)
                deck.deal(player2)
                if not player.stand:
                    player2.ready = False
            else:
                player2.set_stand()

        if (player.stand or player.bust) and (player2.stand or player2.bust):
            check_winner(win, player, player2)
            pre_reset(win, player, player2)


main()
