from uturtle_prof import *


def triangle(t, n, size):
    if n == 0:
        moveForward(t, size)
        turnLeft(t, 120)
        moveForward(t, size)
        turnLeft(t, 120)
        moveForward(t, size)
        turnLeft(t, 120)
    else:
        triangle(t, n-1, size/2)
        moveForward(t, size/2)
        triangle(t, n-1, size/2)
        moveBackward(t, size/2)
        turnLeft(t, 60)
        moveForward(t, size/2)
        turnRight(t, 60)
        triangle(t, n-1, size/2)
        turnLeft(t, 60)
        moveBackward(t, size/2)
        turnRight(t, 60)

if __name__ == '__main__':
    setTitle("Ex 2")
    Matis = umonsTurtle()
    setSpeed(Matis, 0)
    triangle(Matis, 4, 256)
    Matis.color(blue)
    wait()