import turtle


def carre(t, x, seuil):
    third = x / 3.0
    if x < 1:
        return
    if seuil == 0:
        t.forward(third)
        t.left(90)
        t.forward(third)
        t.right(90)
        t.forward(third)
        t.right(90)
        t.forward(third)
        t.left(90)
        t.forward(third)
    else:
        carre(t, third, seuil - 1)
        t.left(90)
        carre(t, third, seuil - 1)
        t.right(90)
        carre(t, third, seuil - 1)
        t.right(90)
        carre(t, third, seuil - 1)
        t.left(90)
        carre(t, third, seuil - 1)


if __name__ == '__main__':
    screen = turtle.Screen()
    turtle.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    t.penup()
    t.goto(0 - 500/2, 0)
    t.pendown()

    carre(t, 500, 6)

    turtle.update()
    turtle.done()