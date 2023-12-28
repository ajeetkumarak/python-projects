import another_module
print(another_module.another_variable)

# construct new object from class

# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("skyBlue","coral")
timmy.speed(55)
# for i in range(1, 99):
#     timmy.forward(144)
#     timmy.left(91)
#     timmy.forward(144)
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.border = False
table.align = "l"
print(table)