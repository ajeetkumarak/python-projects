import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "ajeetkun91@gmail.com"
PASSWORD = "wfjxacwiupetpccx"

# --------------------------         ----------------------
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv('birthdays.csv')
# print(birthdays_data)

birthday_dicts = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dicts:
    birthday_person = birthday_dicts[today_tuple]

    print(birthday_person["year"])
    random_int = random.randint(1, 3)
    file_path = f"letter_templates/letter_{random_int}.txt"

    with open(file_path, "r") as letter_file:
        s = letter_file.read()
        contents = content.replace("[NAME]", birthday_person["name"])
        print(person_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject: Birthday wishes from shree Krishna, \n\n{contents}")


