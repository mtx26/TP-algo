from uturtle_prof import *

def tree(t, x, a, n):
    if n == 0:
        moveForward(t, x)
        turnLeft(t, a/2)
        moveForward(t, x/1.5)
        moveBackward(t, x/1.5)
        turnRight(t, a)
        moveForward(t, x/1.5)
        moveBackward(t, x/1.5)
        turnLeft(t, a/2)
        moveBackward(t, x)
    else:
        moveForward(t, x)
        turnLeft(t, a/2)
        tree(t, x/1.5, a, n-1)
        turnRight(t, a)
        tree(t, x/1.5, a, n-1)
        turnLeft(t, a/2)
        moveBackward(t, x)





if __name__ == '__main__':
    screen = turtle.Screen

    t = turtle.Turtle()
    setSpeed(t, 0)
    turnNorth(t)
    tree(t, 100, 120, 7)
    wait()