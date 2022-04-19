import time as time
from score import Scoreboard
from snake import Snake
from food import Food

snake1 = Snake()
food1 = Food()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    snake1.screen.update()
    time.sleep(0.1)
    snake1.move_snake(20)
    snake1.get_events()
    
    if snake1.snake[0].distance(food1) < 1:
        food1.move()
        snake1.add_snake_part()
        scoreboard.add_point()

    if snake1.snake[0].position()[0] > 280 or snake1.snake[0].position()[0] < -280 or snake1.snake[0].position()[1] > 280 or snake1.snake[0].position()[1] < -280:
        game_is_on = False
        scoreboard.game_over()

    for snake_part in snake1.snake[1:]:
        if snake_part.distance(snake1.snake[0]) < 1:
            game_is_on = False
            scoreboard.game_over()

snake1.screen.exitonclick()