from line import Line
from point import Point


class Cell:
    def __init__(self, win=None):

        self._y1 = None
        self._x1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self, x1, y1, x2, y2):

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(left_wall, None if self.has_left_wall else "white")

        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(right_wall, None if self.has_right_wall else "white")

        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(top_wall, None if self.has_top_wall else "white")

        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(bottom_wall, None if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        move = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        if undo:
            self._win.draw_line(move, "gray")
        else:
            self._win.draw_line(move, "red")
