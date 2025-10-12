import numpy as np
from PIL import Image
import random

w, h = 400, 400
data = np.zeros((h, w, 3), dtype=np.uint8)
for y in range(h):
    for x in range(w):
        r = int((x*y)%255)
        g = int((x+y*2)%255)
        b = random.randint(0, 255)
        data[y, x] = [r, g, b]
img = Image.fromarray(data, 'RGB')
img.save("neural_art.png")
print("AI-style art saved as neural_art.png")