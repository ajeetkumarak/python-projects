from flask import Flask
# from markupsafe import escape

app = Flask(__name__)

print(__name__)


def make_bold(function):
    def wrapper():
        return "<b style='font-size:41px; text-align:center'>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em style='font-size:44px'>" + function() + "</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return ("<u style='font-size:349px;background-color:purple;color:pink"
                "'>") + function() + "</u>"
    return wrapper


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This a a <em><b>paragraph</b></em></p>'
            '<a style="font-size:44px; color:green" href="www.google.com">Google</a>'
            )


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<h1 style='background-color: purple'>Nice to meet you, ..{name.title()}, You are {number} years old.</h1>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "GoodBye"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)

















# Functions     inputs/ functionality / output


# def add(n1, n3):
#     return n1 + n3

#
# def subtract(n1, n3):
#     return n1 - n3
#
#
# def multiply(n1, n3):
#     return n1 * n3
#
#
# def divide(n1, n3):
#     return n1 / n3

#  Python Functions are first-class objects, which can be passed around as arguments
# e.g. - int/str/float etc.
#
# def calculate(calc_function, n1, n3):
#     calc_function(n1, n3)
#
#
# result = calculate(add, 9, 7)
# print(result)
#
#
# # Nested Functions
# def outer_function():
#     print('I m outer.')
#
#     def nested_function():
#         print("I m inner i.e. nested.")
#
#     nested_function()

# outer_function()


# Functions can be returned from other functions
# def return_function():
#     print('I m outer.')
#
#     def nested_function():
#         print("I m inner i.e. nested.")
#
#     return nested_function
#
#
# req_function = return_function()
# req_function()
#
# # Python Decorator Function
#