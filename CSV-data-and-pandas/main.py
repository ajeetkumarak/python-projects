
# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#             print(row[1], row[0])
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather-data.csv")
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list), temp_list)
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
#
# average = data["temp"].mean()
# print(average)
#
# maximum = data["temp"].max()
# print(maximum, data["temp"].min())

# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Tuesday"])
#
# # Get Max temp Data in row
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition, monday.temp)
#
# temp_F = ((monday.temp * 9) / 5) + 32
# print(temp_F)

# # Create a Dataframe from scratch
# data_dict = {
#     "students": ["Amy", "Timmy", "James", "Angela", "Ajeet"],
#     "scores": [78, 89, 49, 73, 79]
# }
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv("new_data.csv")

data = pandas.read_csv("Squirrel_Data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

print(len(gray_squirrels), len(red_squirrels), len(black_squirrels))

squirrels_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [len(gray_squirrels), len(red_squirrels), len(black_squirrels)]
}

# squirrels_data.to_csv("squirrel_count.csv")
df = pandas.DataFrame(squirrels_dict)
df.to_csv("squirrel_count.csv")
