import matplotlib.pyplot as plt

labels = ["Product A", "Product B", "Product C", "Product D",]
sizes = [50, 20, 15, 15]

explode = (0.1, 0, 0, 0)
plt.pie(
    sizes, labels=labels, explode=explode,
    autopct='%1.1f%%', startangle=90
)

plt.title('Exploded Pie Chart - Sales Distribution')
plt.axis('equal')
plt.show()