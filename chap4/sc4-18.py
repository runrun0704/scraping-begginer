import folium

m = folium.Map(location = [35.95601513, 136.17586812], zoom_start = 16)
folium.Marker([35.95604482, 136.17658386]).add_to(m)

m.save("megane.html")