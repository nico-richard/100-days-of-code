import turtle as t
from random import randint, randrange, choice
import colorgram as cg

t1 = t.Turtle()
screen = t.Screen()
colors = cg.extract('day18/image.jpg', 6)

t1.speed(0)
t1.width(10)
t1.penup()
t1.setpos(-200, 200)
t1.hideturtle()
t1.penup()
screen.colormode(255)
screen.bgcolor((210, 210, 210))

for x in range(11):
    for y in range(11):
        t1.dot()
        t1.forward(40)
        y += 1
        # t1.color(tuple(randint(0, 255) for color in range(3)))
        t1.color(choice(colors).rgb)
    t1.right(90)
    t1.forward(40)
    t1.left(90)
    t1.backward(440)
    x += 1

screen.mainloop()