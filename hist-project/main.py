import random
import turtle

import colorgram
from turtle import Turtle, Screen, colormode
turtle.colormode(255)
tim = Turtle()

colors = colorgram.extract('images.jpg', 23)
# print(len(colors))

# all_colors = []
#
# for n in range(1, 23):
#     first_color = colors[n]
#     rgb = first_color.rgb
#     color = (rgb[0], rgb[1], rgb[2])
#     # red = rgb.r
#     # green = rgb.g
#     # blue = rgb.b
#     # print(rgb, red, green, blue)
#     all_colors.append(color)

# print(all_colors)

color_list = [(38, 230, 235), (224, 162, 65), (18, 43, 84), (238, 29, 220), (135, 61, 85), (227, 239, 33), (175, 61, 43), (126, 38, 60), (57, 48, 35), (21, 86, 61), (246, 196, 52), (18, 114, 143), (195, 140, 160), (228, 85, 39), (56, 139, 72), (229, 173, 190), (154, 188, 179), (194, 101, 133), (24, 64, 53), (58, 71, 38), (165, 204, 199), (68, 22, 42)]

tim.speed(9)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.left(135)

# for _ in range(10):
    # for _ in range(10):
    #     tim.dot(20, random.choice(color_list))
    #     tim.forward(50)
    #     tim.dot(20, random.choice(color_list))
    # tim.setheading(90)
    # tim.forward(50)
    # tim.setheading(180)
    # tim.forward(500)
    # tim.setheading(360)

# another Way ********************************
number_of_dots = 100
# tim.pendown()
tim.hideturtle()
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    tim.dot(20, random.choice(color_list))
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()









