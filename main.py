from graphics import Window, Point, Line

point1 = Point(0, 0)
point2 = Point(100, 100)
point3 = Point(69, 96)
point4 = Point(59, 420)
line1 = Line(point1, point2)
line2= Line(point3, point4)

def main():
    win = Window(800, 600)
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.wait_for_close()

main()