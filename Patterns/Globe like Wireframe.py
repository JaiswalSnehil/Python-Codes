from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

phi, theta = np.mgrid[0:np.pi:50j, 0:2*np.pi:50j]
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

ax = plt.figure().add_subplot(111, projection='3d')
ax.plot_wireframe(x,y,z,color='cyan')

plt.show()