import turtle as t
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 30 / 20
CAR_HEIGHT = 20 / 20


class CarManager():

    def __init__(self):
        self.cars = []

    def new_car(self):
        new_car = t.Turtle('square')
        new_car.shapesize(stretch_wid=CAR_HEIGHT, stretch_len=CAR_WIDTH)
        new_car.penup()

        y_pos = randint(-15, 15) * 20
        x_pos = 300
        new_car.goto(x=x_pos, y=y_pos)
        new_car.setheading(180)

        new_car.color(choice(COLORS))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)