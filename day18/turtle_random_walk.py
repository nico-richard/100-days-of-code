import turtle as t
from random import randint, randrange


t1 = t.Turtle()
screen = t.Screen()

t1.speed(0)
t1.width(10)
screen.colormode(255)

for _ in range(1000):
    t1.forward(30)
    t1.setheading(randrange(0, 360, 90))
    t1.color(tuple(randint(0, 255) for color in range(3)))

screen.mainloop()