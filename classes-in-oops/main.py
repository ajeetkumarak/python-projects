class User:

    def __init__(self, user_id, username):
        print("new user being created . . ")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "ajeet")
user_2 = User("111", "angela")

# an attribute is a variable that's associated with an object
# user_1.id = "111"
# user_1.username = "ajeet"


# print(user_1.username)
# print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)
