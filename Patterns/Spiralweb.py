import matplotlib.pyplot as plt
import numpy as np

num_lines = 50
num_turns = 10
num_points = 1000

fig, ax = plt.subplots(figsize=(6,6))
theta = np.linspace(0, num_turns*2*np.pi, num_points)
r = np.linspace(0, 1, num_points)

x = r*np.cos(theta)
y = r*np.sin(theta)
ax.plot(x, y, color='black')

for i in range(num_lines):
    angle = 2*np.pi*i/num_lines
    x_line = [0, np.cos(angle)]
    y_line = [0, np.sin(angle)]
    ax.plot(x_line, y_line, color='black', linewidth=0.8)

ax.axis('off')
plt.show()