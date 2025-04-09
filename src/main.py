from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

point1 = Point(0, 0)
point2 = Point(100, 100)
point3 = Point(100, 0)
point4 = Point(200, 100)
line1 = Line(point1, point2)
line2= Line(point3, point4)

def main():
    num_rows = 5
    num_cols = 5
    margin = 20
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    seed = 1

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)

    win.wait_for_close()

main()