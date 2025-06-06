from tkinter import Tk, Canvas, PhotoImage


class Window:
    """Takes integer height and width inputs to create a standard Tkinter window with a table
    as the background."""

    def __init__(self, height, width):
        self.__root = Tk()
        self.__root.title("Blackjack")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, height=height, width=width)
        self.canvas.pack()
        self.__running = False
        self.img = PhotoImage(file="./static/table.png")

    def close(self):
        self.__running = False

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.__root.update()
            self.__root.update_idletasks()
