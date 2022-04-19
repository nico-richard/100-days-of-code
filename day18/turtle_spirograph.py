import turtle as t
from random import randint as rdint

t1 = t.Turtle()
screen = t.Screen()

t1.speed(0)
t1.width(3)
screen.colormode(255)

for _ in range(100):
    t1.circle(100)
    t1.right(5)
    t1.color(tuple(rdint(0, 255) for color in range(3)))

screen.mainloop()