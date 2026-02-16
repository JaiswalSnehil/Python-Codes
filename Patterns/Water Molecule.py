import py3Dmol
import os
import tempfile

view = py3Dmol.view(width=400, height=300)

view.addModel("""
3
water
O 0.000 0.000 0.000
H 0.958 0.000 0.000
H -0.239 0.927 0.000
""", "xyz")

view.setStyle({'stick':{}})
view.zoomTo()

html = view._make_html()

file_path = os.path.abspath("molecule.html")

with open(file_path, "w") as f:
    f.write(html)

print("Opening:", file_path)
os.system(f"open '{file_path}'")