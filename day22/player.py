import turtle as t

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):

    def __init__(self, start_x, start_y):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.goto(x=start_x, y=start_y)
        self.shape('turtle')
        self.color('black', 'green')

    def move(self):
        self.forward(MOVE_DISTANCE)