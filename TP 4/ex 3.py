from uturtle_prof import *
screen = turtle.Screen

t = turtle.Turtle()
setSpeed(t, 0)
def koch(t, x, seuil):
    if seuil == 0:
        moveForward(t, x/3)
        turnLeft(t, 60)
        moveForward(t, x/3)
        turnRight(t, 120)
        moveForward(t, x/3)
        turnLeft(t, 60)
        moveForward(t, x/3)
    else:
        koch(t, x/3, seuil-1)
        turnLeft(t, 60)
        koch(t, x/3, seuil-1)
        turnRight(t, 120)
        koch(t, x/3, seuil-1)
        turnLeft(t, 60)
        koch(t, x/3, seuil-1)
koch(t, 500, 5)

wait()