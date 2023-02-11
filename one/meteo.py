import requests


URL = "https://api.weatherbit.io/v2.0/current" #Задаем URL
key = "6f605ec8e0eb4f788acf65e8c3f0bebb" # Задаем токен
lang = "ru" # Выбираем необходимый язык
city = "Moscow" # Определяем город
country = "Russia" # Определяем страну
params = {'key':key, 'lang':lang, 'city':city, 'country':country} # передаем все в параметры
response = requests.get(URL, params=params).json() #получаем json response
r_city = response['data'][0]["city_name"] #берем из json город
r_temperature = response['data'][0]["temp"] #берем из json температуру
r_description = response['data'][0]["weather"]["description"] #берем из json описание

print(f'Никита, в городе {r_city} сейчас {r_temperature}, {r_description.lower()}.')