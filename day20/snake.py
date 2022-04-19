from this import d
import turtle as t

class Snake:

    def __init__(self):
        self.snake = []
        self.create_screen()
        self.create_snake(5)
        self.heading = self.snake[0].heading()

    def create_screen(self):
        self.screen = t.Screen()
        self.screen.setup(width=600, height=600)
        self.screen.colormode(255)
        self.screen.bgcolor((50, 50, 50))
        self.screen.title('Snake Game')
        self.screen.tracer(0)
        self.screen.listen()

    def add_snake_part(self):
        snake_part = t.Turtle('square')
        snake_part.penup()
        snake_part.speed(0)
        snake_part.color((200, 200, 200))
        snake_part.speed(1)
        if self.snake == []:
            snake_part.goto(x=0, y=0)
        else:
            snake_part.goto(x=self.snake[-1].xcor(), y=self.snake[-1].ycor())
        self.snake.append(snake_part)
        return snake_part

    def create_snake(self, length):
        for _ in range(length):
            self.add_snake_part()

    def go_right(self):
        if self.heading != 180:
            self.snake[0].setheading(0)
            self.heading = self.snake[0].heading()

    def go_left(self):
        if self.heading != 0:
            self.snake[0].setheading(180)
            self.heading = self.snake[0].heading()

    def go_up(self):
        if self.heading != 270:
            self.snake[0].setheading(90)
            self.heading = self.snake[0].heading()

    def go_down(self):
        if self.heading != 90:
            self.snake[0].setheading(270)
            self.heading = self.snake[0].heading()

    def move_snake(self, distance):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            self.snake[snake_num].goto(self.snake[snake_num - 1].position())
        self.snake[0].forward(distance)

    def get_events(self):
        self.screen.onkeypress(fun=self.go_right, key='Right')
        self.screen.onkeypress(fun=self.go_left, key='Left')
        self.screen.onkeypress(fun=self.go_up, key='Up')
        self.screen.onkeypress(fun=self.go_down, key='Down')