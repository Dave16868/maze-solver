from cell import Cell
import time # CORRECTION: time.sleep() requires time module
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = [] # create cells list in initialisation instead of the method

        self._create_cells()
        self._break_entrance_and_exit() # correct in putting this here

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                c = Cell(self._win)
                column.append(c)
            self._cells.append(column)

        # ? only once the matrix is populated call the draw cell method

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i , j)

    def _draw_cell(self, i , j):
        if self._win is None: # CORRECTION: draw nothing if no window
            return

        x1_pos = self._x1 + (i * self._cell_size_x)
        y1_pos = self._y1 + (j * self._cell_size_y)
        x2_pos = x1_pos + self._cell_size_x
        y2_pos = y1_pos + self._cell_size_y

        cell = self._cells[i][j]
        cell.draw(x1_pos, y1_pos, x2_pos, y2_pos)

        self._animate()
    
    def _animate(self):
        if self._win is None: # CORRECTION: animate nothing if no window
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)