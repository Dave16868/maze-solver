from graphics import Window, Point, Line
from cell import Cell
from maze import Maze
import sys

point1 = Point(0, 0)
point2 = Point(100, 100)
point3 = Point(100, 0)
point4 = Point(200, 100)
line1 = Line(point1, point2)
line2= Line(point3, point4)

def main():
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 1920
    screen_y = 1080
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    seed = 420

    sys.setrecursionlimit(10000)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)
    print("starting maze")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can't be solved")
    else:
        print("maze solved!")

    win.wait_for_close()

main()