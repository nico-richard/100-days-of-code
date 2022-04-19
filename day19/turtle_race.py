import turtle as t
from random import randint, choice, random

screen = t.Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title='Make your choice', prompt="Which turtle will win ? Enter a color (R/G/B/O/Y/P) :")
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
all_turtles = []

for color in colors:
    t1 = t.Turtle()
    t1.penup()
    t1.speed(2)
    t1.shape('turtle')
    t1.color('black', color)
    t1.goto(x=-200, y=-120+colors.index(color)*50)
    all_turtles.append(t1)

# if user_bet:
while True:
    random_distance = randint(0, 20)
    random_turtle = choice(all_turtles)
    random_turtle.forward(random_distance)
    if random_turtle.position()[0] > screen.screensize()[0] / 2:
        random_turtle.write('I won', font=('Arial', 20, 'normal'), align='left')
        break
    
screen.mainloop()