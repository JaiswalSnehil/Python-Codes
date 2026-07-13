import leafmap.foliumap as leafmap
import webbrowser
import os

m = leafmap.Map()

m.add_basemap("HYBRID")

m.add_marker(
    location=[28.6139, 77.2090],
    popup="Delhi"
)

# Save map
outfile = "delhi_map.html"
m.to_html(outfile)

# Open in browser
webbrowser.open("file://" + os.path.abspath(outfile))