from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("My  Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# game start here
game_on = True
while game_on:
    # time.sleep(.001)
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     detect collision on wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # print(l_paddle.distance(ball))

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 30 and ball.xcor() < -330:
        ball.bounce_x()

    # detect ball misses right paddle, left player get one point
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()
        print(scoreboard.l_score)

    # detect ball misses left paddle, right player got one point
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

    if scoreboard.l_score > 5 or scoreboard.r_score > 5:
        scoreboard.game_over()
        game_on = False


screen.exitonclick()
