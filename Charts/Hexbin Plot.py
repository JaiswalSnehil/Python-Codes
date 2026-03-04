import matplotlib.pyplot as plt 
import numpy as np

x = np.random.randn(10000)
y = np.random.randn(10000)

plt.hexbin(x, y, gridsize=30, cmap='Blues')
plt.colorbar(label='Count')

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Hexbin Plot')
plt.show()