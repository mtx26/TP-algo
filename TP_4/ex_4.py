import turtle
from ex_3 import koch


def flocon(t, x, seuil):
    t.penup()
    t.goto(0 - x/2, 0 + x/3)
    t.pendown()

    koch(t, x, seuil)
    t.right(120)
    koch(t, x, seuil)
    t.right(120)
    koch(t, x, seuil)


if __name__ == '__main__':
    screen = turtle.Screen()
    turtle.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    flocon(t, 500, 7)

    turtle.update()
    turtle.done()