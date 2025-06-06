from graphics import Window
from card import Card

win = Window(500, 1000)
win.canvas.create_image(250, 250, image=win.img)

card = Card("jack", "hearts")
win.canvas.create_image(125, 250, image=card.img)

win.wait_for_close()
