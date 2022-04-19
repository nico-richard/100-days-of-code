import turtle as t

t1 = t.Turtle()
screen = t.Screen()
angle = 360 / 3

t1.pencolor('grey')
t1.speed(0)
t1.width(2)

for _ in range(1, 21):

    t1.forward(50)
    t1.right(angle)

    if t1.pencolor() == 'grey':
        t1.pencolor('blue')
    elif t1.pencolor() == 'blue':
        t1.pencolor('grey')

    while abs(t1.pos()) > 1:
        t1.forward(50)
        t1.right(angle)
    angle = 360 / (3 + _)

screen.mainloop()