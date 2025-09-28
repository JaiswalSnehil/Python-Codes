import matplotlib.pyplot as plt

languages = ['JavaScript', 'C++', 'Java', 'Python']
popularity = [80, 57, 65, 90]

plt.barh(languages, popularity, color='orange')
plt.title('Horizontal Bar Chart')
plt.show()