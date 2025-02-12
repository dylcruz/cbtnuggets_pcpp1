import requests

# response = requests.get('https://restcountries.com/v3.1/name/usa')
# country_info = response.json()[0]

# print(f'The capital of the country is: {country_info["capital"]}')
# print(f'The population of the country is: {country_info["population"]}')

response = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=6b93dacdbf588191a63a3f6040fb55da')

weather_data = response.json()

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * (9/5) + 32

for data_point in weather_data['list']:
    print(f'{data_point["dt_txt"]}: {float(kelvin_to_fahrenheit(data_point["main"]["temp"]))}')
