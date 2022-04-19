import turtle as t

t1 = t.Turtle()
screen = t.Screen()

def move_forward():
    t1.forward(10)

def turn_right():
    t1.left(10)

def turn_left():
    t1.right(10)

screen.listen()
screen.onkeypress(key='Up', fun=move_forward)
screen.onkeypress(key='Left', fun=turn_right)
screen.onkeypress(key='Right', fun=turn_left)

screen.mainloop()