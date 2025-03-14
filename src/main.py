from window import Window
from line import Line
from point import Point
from cell import Cell

point_1 = Point(5, 300)
point_2 = Point(100, 200)
point_3 = Point(100, 450)
line = Line(point_1, point_3)
line_2 = Line(point_2, point_3)


win = Window(800, 600)

cell_1 = Cell(Point(50, 50), Point(150, 150), win)
cell_2 = Cell(Point(200, 50), Point(300, 150), win)

cell_1.draw()
cell_2.draw()

win.wait_for_close()
