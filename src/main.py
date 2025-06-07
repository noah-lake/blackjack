from tkinter import Button
from graphics import Window
from card import Deck
from player import Player
from time import sleep


def check_winner(win, player, player2):
    """Determines the winner of the game and displays it on screen."""
    # If both players have the same score, it's a draw. Because busting sets your score to zero,
    # if both players bust, it is still a draw.
    if player.score == player2.score:
        win.canvas.create_text(
            win.width // 2, 100, text="DRAW", anchor="center", font="Calibri 30 bold"
        )
    # If player one's score is higher than player two's score, player one wins.
    elif player.score > player2.score:
        win.canvas.create_text(
            win.width // 2,
            100,
            text="PLAYER 1 WINS",
            anchor="center",
            font="Calibri 30 bold",
        )
    # Otherwise, player two wins.
    else:
        win.canvas.create_text(
            win.width // 2,
            100,
            text="PLAYER 2 WINS",
            anchor="center",
            font="Calibri 30 bold",
        )


def pre_reset(win, player, player2):
    """Creates a reset button at the bottom of the screen."""
    reset_button = Button(
        win.root,
        text="Reset",
        # When the button is pressed, it resets the window, players, and deck objects,
        # destroys itself, and reopens the main menu.
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
    # Reset all of the core objects to their base values.
    win.reset(player, player2)
    deck.reset(player, player2)
    player.reset()
    player2.reset()


# The core objects
win = Window(1700, 640)
player = Player("left", win)
player2 = Player("right", win)
deck = Deck()


def main():
    win.main_menu(deck, player, player2)

    while win.running:
        # Update the screen
        win.root.update()
        win.root.update_idletasks()
        # Logic loop for the computer player.
        # If the player is not drawing more cards, the computer is always ready
        if player.bust or player.stand:
            player2.ready = True
        # If player2 is a computer and is ready to draw:
        if not player2.active and player2.ready:
            # If the player is done drawing and the computer's score is higher, then the computer is done drawing.
            if (player.bust or player.stand) and player2.score > player.score:
                player2.set_stand()
            # If the computer's score is less than 17 or the player is done drawing and the computer's score
            # is less than the players, draw a card.
            elif player2.score < 17 or (player.stand and player2.score < player.score):
                sleep(0.5)
                deck.deal(player2)
                # Then, if the player is still drawing, the computer waits.
                if not player.stand:
                    player2.ready = False
            # If the compuere's score is more than 17 and is higher than the player's score while the player is
            # still drawing, the computer plays it safe and stands.
            else:
                player2.set_stand()

        # If both players are done drawing, display the winner and display the reset button.
        if (player.stand or player.bust) and (player2.stand or player2.bust):
            check_winner(win, player, player2)
            pre_reset(win, player, player2)


main()
