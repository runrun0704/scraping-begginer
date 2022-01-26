import pandas as pd
import folium

df = pd.read_csv("店舗.csv")

store = df[["緯度", "経度", "店舗名"]].values

m = folium.Map(location = [35.956477, 136.184073], zoom_start = 16)
for data in store:
    folium.Marker([data[0], data[1]], tooltip = data[2]).add_to(m)
m.save('store.html')    