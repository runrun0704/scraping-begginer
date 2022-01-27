import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=meric"
url = url.format(city="Kobe,JP", key="c966fe8f26043aab0f015030590acd02")

jsondata = requests.get(url).json()
print(jsondata)