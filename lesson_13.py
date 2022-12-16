#1 встроенные datatime() math(sqrt)
 
# import math
# print(math.sqrt(9))

# from math import sqrt, pi
# print(math.pi)
# print(sqrt(9))
# print(pi)

# import lesson_12t
# print(lesson_12t.a)

# from lesson_12t import r
# r(46)

# from lesson_12t import People
# a = People('Elmo', 15)
# print(a)

import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()

window.bgcolor("black")


def polygon(n, size=80):
    if n > 2:
        angle = 360 / n

        for n in range(0, n):
            turtlePen.left(angle)
            turtlePen.forward(size)


turtlePen.speed(100)

colors = ['orange', 'cyan', 'blue', 'green', 'red']

size = 40

for i in range(0, 60):
    turtlePen.color(colors[i % 5])
    polygon(4, size)
    turtlePen.left(5)
    size = size + 3

window.mainloop()
