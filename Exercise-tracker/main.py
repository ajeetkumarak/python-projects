import requests
from datetime import datetime

# Nutritionix APP ID and API Key. Actual values are stored as environment variables.
APPLICATION_ID = "987a1ee1"
APPLICATION_KEY = "b2e38f399cc673fcbcd4ab9d303fb74d"

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 49
HEIGHT_CM = 145
AGE = 19

print(type(WEIGHT_KG))
exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell me which exercise you did:  ")

# Nutritionix API Call
headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY,
    # "x-remote-user-id": "0",
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# datetime module
today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")
print(today_date, now_time)

# Sheety API Call & Authentication
GOOGLE_SHEET_NAME = "workouts"

sheety_endpoint = "https://api.sheety.co/410ae2266d80371e95a9306c2aee01bf/workoutTracking/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    # print(sheet_inputs)
    # # Sheety Authentication Option 1: No Auth
    # sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs)
    # print(sheet_response.json())


# Sheety Authentication Option 2: Basic Auth
    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs,
                                   auth=("ajeetkraj", "jeetbr24m0372"))


    print(sheet_response.text)







