import json
from pprint import pprint

with open("test2.json", mode = "r") as f:
    jsondata = json.loads(f.read())
    print("一つめのオブジェクト", jsondata[0])
    print("都市名", jsondata[0]["name"])
    print("緯度", jsondata[0]["coord"]["lat"])