import folium

m = folium.Map(location=[20.5937, 78.9629], zoom_start=4)

folium.Marker(
    location=[28.6139, 77.2090],
    popup= 'New Delhi',
    tooltip= 'Captial of India'
).add_to(m)

m.save('india_map.html')
print("Map created! Open india_map.html")
m