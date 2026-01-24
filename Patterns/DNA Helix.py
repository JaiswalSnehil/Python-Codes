import py3Dmol, math, webbrowser, tempfile

v = py3Dmol.view(width=400, height=400)

for i in range(40):
    x = math.cos(i/3)
    y = math.sin(i/3)
    z = i*0.2
    v.addSphere({"center":{ "x":x,"y":y,"z":z},
        "radius":0.3,"color":"orange"})
    v.addSphere({"center":{ "x":-x,"y":-y,"z":z},
        "radius":0.3,"color":"cyan"})
v.setBackgroundColor("black")
v.zoomTo()

html = v._make_html()

with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
    f.write(html)
    webbrowser.open('file://' + f.name)