import requests
import json
from pprint import pprint

url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=meric"
url = url.format(city = "Tokyo,JP", key = "c966fe8f26043aab0f015030590acd02")

jsondata = requests.get(url).json()
pprint(jsondata)