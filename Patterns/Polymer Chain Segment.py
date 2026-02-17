import py3Dmol
import os
import tempfile

view = py3Dmol.view(600, 600)

view.addModel("""8
polymer
C 0 0 0
C 1.5 0 0
C 3 0 0
C 4.5 0 0
H 0 -1 0
H 1.5 1 0
H 3 -1 0
H 4.5 1 0
""", "xyz")

view.setStyle({'stick':{},'sphere':{'scale':0.3}})
view.zoomTo()
view.spin(True)

html = view._make_html()

file_path = os.path.abspath("molecule.html")

with open(file_path, "w") as f:
    f.write(html)

print("Opening:", file_path)
os.system(f"open '{file_path}'")