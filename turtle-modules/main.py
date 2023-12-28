# we also import as...(if name of module is big) -- called "Aliasing Modules"
import turtle
import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Making a Spirograph
timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        curr_heading = timmy.heading()
        timmy.setheading(curr_heading + size_of_gap)

draw_spirograph(4)

# random walk code hear
timmy.pensize(11)
timmy.speed(10)
directions = [0, 90, 180, 270]

# for _ in range(444):
#     timmy.forward(25)
#     timmy.setheading(random.choice(directions))
#     timmy.color(random_color())
#

# **************************************************************
# for i in range(3, 15):
#     print(i)
#     timmy.color("purple")
#     for _ in range(i):
#
#         timmy.forward(111)
#         timmy.left(360 / i)
#         timmy.color("skyBlue")
#         # timmy.forward(111)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(111)
        timmy.right(angle)


colors = [
    "#FF0000",
    "#00FF00",
    "#0000FF",
    "#FFFF00",
    "#FF00FF",
    "#FFA500",
    "#800080",
    "#008000",
    "#000080",
    "green",
    "purple",
    "yellow"
]
# for shape_sides in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_sides)
#     # timmy.color(colors[shape_sides - 3])



# tom = Turtle()
# # tom.shape('triangle')
# tom.color("black")
# tom.speed(53)
# for _ in range(54):
#     tom.forward(11)
#     tom.penup()
#     tom.forward(11)
#     tom.pendown()

# for _ in range(100):
#     timmy.forward(200)
#     timmy.right(91)
#     tom.forward(-200)
#     tom.right(91)
#     timmy.back(100)
#     tom.forward(100)

screen = Screen()
screen.exitonclick()

