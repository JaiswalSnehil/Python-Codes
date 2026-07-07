import polyscope as ps
import numpy as np

ps.init()

points = np.random.rand(1000, 3)

cloud = ps.register_point_cloud("Random Point Cloud", points)
cloud.set_radius(0.005)

print("Opening window...")

ps.show()

print("Program finished.")