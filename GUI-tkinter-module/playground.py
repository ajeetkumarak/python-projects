# UNLIMITED POSITIONAL ARGUMENTS

# * the number of arguments for the function vary because the asterix operator collects all the arguments in tuple
def add(*args):
    print(args[1])
    print(args)
    # print(sum(args))
    sum = 0
    for n in args:
        # print(n)
        sum += n
    return sum

print(add(7,8,9,7,8,55,8,95,1,8,9,9))

# DOUBLE ASTERIX OPERATOR I.E.   **kwargs   (Keywords arguments)
# This allows us to work with an arbitrary number of keyword arguments


def calculate(n, **kwargs):
    print(type(kwargs))

    # for key, value in kwargs.items():
    #     print(key, value)

    # print(kwargs["add"],  kwargs["multiply"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=9, multiply=7)


class Car:

    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # use get() method  -- Not give error if any arg not given
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")

print(my_car.model, my_car.make)
