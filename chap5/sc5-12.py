import requests
import json
from datetime import datetime, timedelta, timezone
from pprint import pprint
import pandas as pd


url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=meric"
url = url.format(city = "Tokyo,JP", key = "c966fe8f26043aab0f015030590acd02")

jsondata = requests.get(url).json()
df = pd.DataFrame(columns = ["気温"])
tz = timezone(timedelta(hours=+9), 'JST')
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    temp = dat["main"]["temp"]
    df.loc[jst] = temp

pprint(df)

