import matplotlib.pyplot as plt

data = [7,8,5,6,9,10,6,7,8,9,5,7,8,10,6]
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title('Histogram of Data')
plt.show()