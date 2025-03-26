from cell import Cell
import time
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self.cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        exit_cell = self.cells[-1][-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(len(self.cells) - 1, len(self.cells[0]) - 1)

    def _break_walls_r(self, i, j):
        current_cell = self.cells[i][j]
        current_cell.visited = True

        while True:
            to_visit = []

            if i > 0 and not self.cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self.cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            random_index = random.randrange(len(to_visit))
            next_i, next_j = to_visit[random_index]

            if next_j == j + 1:
                self.cells[i][j].has_top_wall = False
                self.cells[next_i][next_j].has_bottom_wall = False

            if next_j == j - 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[next_i][next_j].has_top_wall = False

            if next_i == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[next_i][next_j].has_left_wall = False

            if next_i == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[next_i][next_j].has_right_wall = False

            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # left
        if (
            i > 0
            and not self.cells[i][j].has_left_wall
            and not self.cells[i - 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i - 1][j], True)

        # right
        if (
            i < self.num_cols - 1
            and not self.cells[i + 1][j].visited
            and not self.cells[i][j].has_right_wall
        ):
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            current_cell.draw_move(self.cells[i + 1][j], True)

        # top

        if (
            j > 0
            and not self.cells[i][j + 1].visited
            and not self.cells[i][j].has_top_wall
        ):
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j + 1], True)

        # bottom
        if (
            j < self.num_rows - 1
            and not self.cells[i][j - 1].visited
            and not self.cells[i][j].has_bottom_wall
        ):
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j - 1], True)

        else:
            return False

    

    def solve(self):
        return self._solve_r(0, 0)

    def _has_no_wall(self, current_cell, adjacent_cell, direction):
        if direction == "top":
            return not current_cell.has_top_wall and not adjacent_cell.has_bottom_wall
        if direction == "bottom":
            return not current_cell.has_bottom_wall and not adjacent_cell.has_top_wall
        if direction == "left":
            return not current_cell.has_left_wall and not adjacent_cell.has_right_wall
        if direction == "right":
            return not current_cell.has_right_wall and not adjacent_cell.has_left_wall
