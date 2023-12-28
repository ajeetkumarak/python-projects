# FileNotFoundError
# with open("data.txt", "r") as file:
#     file.read()
#

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_exist_key"]

# IndexError
# fruit_list = ["Apple","Orange","Banana"]
# fruit = fruit_list[4]

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     # print(a_dict["dfsdgf"])
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something here..")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     raise TypeError("This is an error that i made up.")



# /////////////////////////////////////
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height never exceed more than 3 meters")

bmi = weight / height ** 2
print(bmi)

