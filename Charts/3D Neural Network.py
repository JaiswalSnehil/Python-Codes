import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
points = np.random.rand(20,3)*5
ax.scatter(points[:,0], points[:,1], points[:,2], s=60)
for i in range(len(points)):
    for j in range(i+1, len(points)):
        if np.random.rand() < 0.2:
            ax.plot([points[i,0],points[j,0]],
                    [points[i,1],points[j,1]],
                    [points[i,2],points[j,2]])
ax.set_title('3D Neural Network')
ax.set_axis_off()
plt.show()