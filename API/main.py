import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "ajeetkun91@gmail.com"
PASSWORD = "wfjxacwiupetpccx"

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response.status_code)
# # data = response.json()["iss_position"]
# # print(data)
# # if not get response----
# response.raise_for_status()

SSM_LAT = 24.9535
SSM_LONG = 84.0143

MY_LAT = 28.679079
MY_LONG = 77.069710


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    # iss_position = (latitude, longitude)
    # print(iss_position)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
# --------------------- - - -- - - - - sunset-sunrise api - - - -- ---------------


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    # print(sunrise)
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    print(type(sunrise_hour), sunset_hour)

    time_now = datetime.now().hour
    # print(time_now.hour)
    if time_now >= sunset_hour or time_now <= sunrise_hour:
        # it's DARK
        print("Dark")
        return True


while True:
    time.sleep(100)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP(smtp.gmail.com) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="jeetaj9162@gmail.com",
                                msg="Subject: ISS here, Look Up \n\nThe ISS is above you in sky..")

