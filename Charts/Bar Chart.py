import matplotlib.pyplot as plt

categories = ['A','B','C','D']
values = [25, 40, 30, 20]

plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()