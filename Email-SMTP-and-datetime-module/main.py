import smtplib
import random

MY_EMAIL = "ajeetkun91@gmail.com"
PASSWORD = "wfjxacwiupetpccx"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="jeetaj9162@gmail.com",
#                         msg="Subject: Hello World\n\nThis is the body of my email.")
#


import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# if year == 2020:
#     print("Wear Mask")
# print(day_of_week, type(year))
#
# date_of_birth = dt.datetime(year=1999, month=11, day=1, hour=14)
# print(date_of_birth)

# -------------------------                      -------------------------------

# with open('quotes.txt', "r") as data_file:
#     data = data_file.readlines()
#     quote = random.choice(data)
#     # quotes_list = [line for line in data_file.readlines()]
#     # today_quote = random.choice(quotes_list)
#     print(quote)

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 6:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="jeetaj9162@gmail.com",
                            msg=f"Subject: Sunday Motivation\n\n{quote}")
