import py3Dmol, random, webbrowser, tempfile
from IPython.display import display

v = py3Dmol.view(width=400, height=400)

for _ in range(100):
    v.addSphere({
        "center":{
            "x":random.uniform(-2,2),
            "y":random.uniform(-2,2),
            "z":random.uniform(-2,2)
        },
        "radius":0.3,
        "color":"gold"
    })
v.setBackgroundColor("black")
v.zoomTo()

html = v._make_html()

with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
    f.write(html)
    webbrowser.open('file://' + f.name)