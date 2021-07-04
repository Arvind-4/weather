import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('API_KEY')
print(api_key)

def get_weather_data(city):
	url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
	data = requests.get(url)
	# pprint(data)

	if data.status_code in range(200, 350):
		data = data.json()

		context = {
			'city': city,
			'country_code': data['sys']['country'],
			'temperature': data['main']['temp'],
			'temperature_max': data['main']['temp_max'],
			'temperature_min': data['main']['temp_min'],
			'temperature_feels_like': data['main']['feels_like'],
			'pressure': data['main']['pressure'],
			'humidity': data['main']['humidity'],
			'main': data['weather'][0]['main'],
			'description': data['weather'][0]['description'].capitalize(),
			'icon': data['weather'][0]['icon'],
			'wind_degree': data['wind']['deg'],
			'wind_speed': data['wind']['speed'],
			'latitude': data['coord']['lat'],
			'longitude': data['coord']['lon'],
			}
		return context

	else:
		return None

print(get_weather_data('chennai'))

# def get_data(city):
# 	url = f'api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
# 	r = request