import turtle


my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
    my_turtle.right(90)
    draw_spiral(my_turtle, line_len-5)


draw_spiral(my_turtle, 100)
my_win.exitonclick()


def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-15, t)
        t.left(40)
        tree(branch_len-10, t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()


def draw_triangle(points, color):
    t.fillcolro(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()



def get_mid(p1, p2):
    return((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(ponits, degree, my_turtle):
    color_map = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    draw_triangle(ponits, color_map[degree], my_turtle)
    if degree > 0:
        sierpinski([points[0], get_mid(points[0], ponits[1]), get_points(ponits[0], points[2])], degree-1, my_turtle)
        sierpinski([points[1], get_mid(points[0], ponits[1]), get_points(ponits[1], points[2])], degree-1, my_turtle)
        sierpinski([points[2], get_mid(points[2], ponits[1]), get_points(ponits[0], points[2])], degree-1, my_turtle)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(my_points, 3, my_turtle)

main()

