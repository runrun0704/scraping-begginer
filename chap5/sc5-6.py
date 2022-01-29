import requests
import json
from pprint import pprint

url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=meric"
url = url.format(city = "Kobe,JP", key = "c966fe8f26043aab0f015030590acd02")

jsondata = requests.get(url).json()
print("都市名", jsondata["name"])
print("気温", jsondata["main"]["temp"])
print("天気", jsondata["weather"][0]["main"])
print("天気詳細", jsondata["weather"][0]["description"])