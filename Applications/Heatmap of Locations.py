import folium
from folium.plugins import HeatMap

m = folium.Map(location=[20,0], zoom_start=2)
data = [
    [28.6139, 77.2090],
    [19.0760, 72.8777],
    [51.5074, -0.1278],
    [40.7128, -74.0060]
]
HeatMap(data).add_to(m)
m.save('heatmap.html')
m