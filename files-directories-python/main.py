# file = open("file.txt")
# contents = file.read()
# print(contents)
# file.close()

# note - Always close the file you open

# best way to open and read files  -- with this if file not exist, then it will create it
with open("file.txt") as file:
    contents = file.read()
    print(contents)

# write in file  here, it will delete previous contents of file and write new
with open("file.txt", "w") as file:
    file.write("New Text.")

# to add contents in file use "a" means "append"
with open("file.txt", "a") as file:
    file.write("\nNice one to study python.")

# it will create the file if not exist note: it will work in only write mode i.e. mode="w"
with open("new_file.txt", mode="w") as file:
    file.write("AS i say, it will create the file if not exist as given name")
