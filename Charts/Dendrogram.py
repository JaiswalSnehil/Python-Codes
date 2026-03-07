import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

np.random.seed(42)
data = np.random.rand(10, 4)

linked = linkage(data, method='ward')

plt.figure(figsize=(8, 5))
dendrogram(linked)
plt.title('Dendrogram - Hierarchical Clustering')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()