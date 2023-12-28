from turtle import Turtle, Screen
import  random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("MAke your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "orange", "blue", "purple", "yellow"]
y_positions = [-100, -60, -20, 20, 60, 100]

# tim = Turtle(shape="turtle")
# tim.goto(x=-230, y=-100)

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() == 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            # print(winning_color)
            if winning_color == user_bet:
                print(f"🎉🎉 You've won, the {winning_color} turtle is winner!")
            else:
                print(f"😌😌 You've lost, the {winning_color} turtle is winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
























# practicing graphics of turtle module
# def add(n1, n3):
#     return n1 + n3
#
# def calculator(n1, n3, fun):
#     return fun(n1, n3)
#

# caculate = calculator(8, 9, add)
# print(caculate)
# def move_forward():
#     tim.forward(11)
#
# def move_backward():
#     tim.backward(11)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
#


screen.exitonclick()
