import requests

# response = requests.get('https://restcountries.com/v3.1/name/usa')
# country_info = response.json()[0]

# print(f'The capital of the country is: {country_info["capital"]}')
# print(f'The population of the country is: {country_info["population"]}')

response = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=6b93dacdbf588191a63a3f6040fb55da')