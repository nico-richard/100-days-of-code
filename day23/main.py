import time
from turtle import Screen

from random import randint
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

turtle1 = Player(0, - SCREEN_HEIGHT / 2 + 20)

cars1 = CarManager()

game_is_on = True

cars = []

while game_is_on:

    count = randint(0, 5)
    if not count:
        cars1.new_car()
    else:
        time.sleep(0.1)
        screen.update()
        cars1.move()

    screen.onkeypress(fun=turtle1.move, key='space')

screen.exitonclick()