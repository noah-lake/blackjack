from graphics import Window
from card import Deck
from player import Player

win = Window(1700, 640)
# win.canvas.create_text(850, 320, text="B L A C K J A C K", fill="red", font=("Arial", 40, "bold"))
player = Player("left", win)
player2 = Player("right", win)
player2.active = True
deck = Deck()

win.start_game(player=player, deck=deck, player2=player2)


win.wait_for_close()
