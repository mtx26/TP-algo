import turtle

def tree(t, x, a, n):
    if x < 1:
        return
    if n == 0:
       t.forward(x)
       t.left(a / 2.0)
       t.forward(x / 1.5)
       t.backward(x / 1.5)
       t.right(a)
       t.forward(x / 1.5)
       t.backward(x / 1.5)
       t.left(a / 2.0)
       t.backward(x)
    else:
       t.forward(x)
       t.left(a / 2.0)
       tree(t, x / 1.5, a, n - 1)
       t.right(a)
       tree(t, x / 1.5, a, n - 1)
       t.left(a / 2.0)
       t.backward(x)





if __name__ == '__main__':
    screen = turtle.Screen()

    turtle.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.setheading(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    tree(t, 200, 180, 20)

    turtle.update()
    turtle.done()