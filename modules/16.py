import math
import random
import requests

KEY = '186a2ae6b4e4a7465105495e3430df15'
URL = 'https://api.openweathermap.org/data/2.5/weather'
city = "Astana"
params = {
    'q': city,
    'appid': KEY,
    'units': 'metric',
}
data = requests.get(URL, params=params)
print(data.json())


print(math.pi)
print(random.randint(0, 100))