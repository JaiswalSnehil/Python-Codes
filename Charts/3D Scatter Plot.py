import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)

ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
ax.set_zlabel("Z Values")
ax.set_title("3D Scatter Plot Example")

plt.show()