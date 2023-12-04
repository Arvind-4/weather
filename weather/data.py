import requests
from decouple import config

API_KEY = config("DJANGO_WEATHER_API_KEY", cast=str)


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    data = requests.get(url)
    if data.status_code in range(200, 350):
        data = data.json()
        context = {
            "city": city,
            "country_code": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "temperature_max": data["main"]["temp_max"],
            "temperature_min": data["main"]["temp_min"],
            "temperature_feels_like": data["main"]["feels_like"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "main": data["weather"][0]["main"],
            "description": data["weather"][0]["description"].capitalize(),
            "icon": data["weather"][0]["icon"],
            "wind_degree": data["wind"]["deg"],
            "wind_speed": data["wind"]["speed"],
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"],
        }
        return context
    return None
