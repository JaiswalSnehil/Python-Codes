import pandas as pd
import numpy as np
import os

conf = pd.DataFrame(
    np.round(np.random.rand(5,5), 2),
    columns=["Cat","Dog","Car","Tree","Human"]
)

html = conf.style \
    .background_gradient(cmap="viridis") \
    .set_caption("AI Confidence Matrix") \
    .to_html()

file_path = os.path.abspath("confidence_matrix.html")

with open(file_path, "w") as f:
    f.write(html)

print("File created at:", file_path)

# macOS guaranteed open
os.system(f"open '{file_path}'")