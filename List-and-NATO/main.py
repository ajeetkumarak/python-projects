import random

# For LIST
# new_list = [item for item in list]
numbers = [1, 3, 4, 5, 6]

num_list = [n*4 for n in numbers]
# print(num_list)

new_n = [n+9 for n in numbers]
name = "Angela"
new_list = [letter for letter in name]
new_num = [n for n in range(1, 5)]
new_num1 = [n * 2 for n in range(1, 5)]
names = ["Ajeet", "Ankit","Anup","Anshu","Abhi","cute"]
short_names = [name for name in names if len(name) <= 4]
upper_names = [name.upper() for name in names if len(name) > 4]

count = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_count = [num**2 for num in count]
squared = [num * num for num in count]
even_num = [num for num in count if num % 2 == 0]

# For DICTIONARIES
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key: new_value for(key, value) in dictionary.items()}

students_scores = {student: random.randint(1, 100) for student in names}
passed = {student: score for (student, score) in students_scores.items() if score > 55}
# print(passed)

# ///////////////////////////////////////////////////////
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 37,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_f = {day: (temp_c * 9)/5 + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

# **********************************************************************************
# How to iterate over pandas dataframe
student_dict = {
    "student": ["Ajeet", "Angela", "Ankit"],
    "score": [78, 89, 94]
}
# looping through dictionary
# for (key, value) in student_dict.items():
#      # print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through a data frame
# for (key, value) in student_data_frame.items():
    # print(value)


# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    print(row.student)
    print(row.score)