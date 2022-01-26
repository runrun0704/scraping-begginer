import pandas as pd
import folium

df = pd.read_csv("消火栓.csv", encoding = "shift-jis")

hydrant = df[["緯度", "経度"]].values

m = folium.Map(location = [35.95601513, 136.17586812], zoom_start = 16)
for data in hydrant:
    folium.Marker([data[0], data[1]]).add_to(m)
m.save('hydrant.html')  