import requests
import json
from datetime import datetime, timedelta, timezone

url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=meric"
url = url.format(city = "Tokyo,JP", key = "c966fe8f26043aab0f015030590acd02")

jsondata = requests.get(url).json()
tz = timezone(timedelta(hours=+9), 'JST')
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"]
    print("日時:{jst}, 天気:{w}, 気温:{t}度".format(jst = jst, w = weather, t = temp))

