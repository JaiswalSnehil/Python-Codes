import folium, random, webbrowser, tempfile, os

m = folium.Map(location=[28.6,77.2], zoom_start=11)

for i in range(20):
    val = random.randint(20, 100)
    folium.CircleMarker(
        location=[28.6+random.uniform(-0.1,0.1),
                  77.2+random.uniform(-0.1,0.1)],
        radius=6, color='green' if val<50 else 'red',
        fill=True, popup=f"Sensor Value: {val}"
    ).add_to(m)

#m.save("sensor_map.html")
tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
tmp.close()

# save map to that file
m.save(tmp.name)

# open in browser
webbrowser.open("file://" + os.path.abspath(tmp.name))