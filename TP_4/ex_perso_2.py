import turtle

def golden_number(t, x, seuil):
    phi = (1 + 5 ** 0.5) / 2
    print(phi)
    if x < 0:
        return
    if seuil == 0:
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x * phi)
        t.right(90)
        t.forward(x)
    else:
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x)
        t.right(90)
        t.forward(x * phi)
        t.right(90)
        golden_number(t, x * phi - x, seuil-1)


if __name__ == '__main__':
    screen = turtle.Screen()

    turtle.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(-300, 300)
    t.pendown()

    golden_number(t, 600, 20)

    turtle.update()
    turtle.done()