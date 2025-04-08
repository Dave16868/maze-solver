from graphics import Line, Point

# CORRECTION: cell not part of graphics

class Cell():
    def __init__(self, win=None): # CORRECTION: create cell in window only, no need input walls or coordinates
        self.has_left_wall = True # CORRECTION: walls true by default
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None 
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2): # cell draws from itself while line is drawn by window?
        if self._win is None: # CORRECTION: draw nothing if cell not in window
            return
        self._x1 = x1 # CORRECTION: coordinates only enter when drawing
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall == True:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)

        if self.has_left_wall == False:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")

        if self.has_right_wall == True:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)

        if self.has_right_wall == False:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        if self.has_top_wall == True:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)

        if self.has_top_wall == False:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.has_bottom_wall == True:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

        if self.has_bottom_wall == False:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False): # SUGGESTION: can use abs() to ensure absolute(positive) value only
        if undo == False:
            line_color = "red"
        if undo == True:
            line_color = "gray"
        p1 = Point(abs((self._x2 - self._x1)) // 2 + self._x1, abs((self._y2 - self._y1)) // 2 + self._y1)
        p2 = Point(abs((to_cell._x2 - to_cell._x1)) // 2 + to_cell._x1, abs((to_cell._y2 - to_cell._y1)) // 2 + to_cell._y1)
        line = Line(p1, p2)
        self._win.draw_line(line, line_color)