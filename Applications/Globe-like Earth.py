import folium
import numpy as np
import webbrowser
import os

m = folium.Map(
    location=[0, 0],
    zoom_start=2,
    tiles="CartoDB dark_matter"
)
for i in range(400):
    lat = np.random.uniform(-70, 70)
    lon = np.random.uniform(-180, 180)
    folium.CircleMarker(
        location=[lat, lon], radius=2,
        color="cyan", fill=True, fill_opacity=0.7
    ).add_to(m)

file_path = os.path.abspath("folium_map.html")
m.save(file_path)

print("Map saved at:", file_path)

# Force open in default browser (macOS reliable way)
os.system(f"open '{file_path}'")