from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(.2)

    snake.move()

    # detect collision with food: *****
    # print(snake.head.distance(food) < 15)
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    #     Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # scoreboard.game_over()
        # game_on = False
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail of snake i.e.
    #    if head collides with any segment in the tail then ,trigger game over
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass---------------------here, we use *** slicing in python ***
        if snake.head.distance(segment) < 10:
            # game_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
