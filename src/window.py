from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):

        self.__root = Tk()
        self.__root.title = "Amaze"
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window closed...")

    def draw_line(self, line, fill_colour="black"):
        line.draw(self.__canvas, fill_colour)

    def close(self):
        self.__is_running = False
