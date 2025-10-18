import turtle


def koch(t, x, seuil):
    third = x / 3.0
    if x < 1:
        return
    if seuil == 0:
        t.forward(third)
        t.left(60)
        t.forward(third)
        t.right(120)
        t.forward(third)
        t.left(60)
        t.forward(third)
    else:
        koch(t, third, seuil - 1)
        t.left(60)
        koch(t, third, seuil - 1)
        t.right(120)
        koch(t, third, seuil - 1)
        t.left(60)
        koch(t, third, seuil - 1)


if __name__ == '__main__':
    screen = turtle.Screen()
    turtle.tracer(0, 0) 

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    t.penup()
    t.goto(-500, 0)
    t.pendown()

    koch(t, 1000, 8)

    turtle.update()
    turtle.done()