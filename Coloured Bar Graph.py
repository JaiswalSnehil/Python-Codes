import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 20]

colors = ['red', 'blue', 'green', 'yellow', 'purple']

plt.bar(categories, values, color=colors)

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Coloured Bar Graph')
plt.show()