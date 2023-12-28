import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "bd5fe2e1f26dcd443a22fb409efa6de1"
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
weather_params = {
    "lat": 51.517351,
    "lon": -0.137758,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
data = response.json()
print(data)
