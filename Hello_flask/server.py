from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    now = datetime.now()
    current_year = now.strftime("%Y")
    random_number = random.randint(1, 11)
    return render_template("test.html",  year=current_year, num=random_number)


@app.route("/guess/<name>")
def guess(name):
    current_year = datetime.now().strftime("%Y")
    age_response = requests.get(url=f"https://api.agify.io/?name={name}")
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    return render_template("guess.html",
                           age_data=age_response.json(),
                           gender_data=gender_response.json(),
                           person_name=name, year=current_year)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/3aad5b98824703e6eccc"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)












































# import random
# from turtle import Turtle, Screen
#
# colors = ['purple', 'green', 'yellow', 'blue', 'red', 'orange', 'pink']
# tim = Turtle()
# tim.pensize(4)
# tim.speed(9)
#
# def square():
#     tim.forward(311)
#     tim.right(97)
#     tim.forward(311)
#     tim.right(99)
#     tim.forward(311)
#     tim.right(99)
#     tim.forward(311)
#     tim.right(99)
#
#
# for _ in range(111):
#     tim.pencolor(random.choice(colors))
#     square()
#     tim.forward(111)
#     tim.setheading(181)
#
# screen = Screen()
# screen.exitonclick()
