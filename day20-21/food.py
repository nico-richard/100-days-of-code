import turtle as t
import random

class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color('black', 'green')

        self.move()

    def move(self):
        xpos = random.randint(-14, 14) * 20
        ypos = random.randint(-14, 14) * 20
        self.setposition(x=xpos, y=ypos)