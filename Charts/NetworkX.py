import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1,2),(2,3)])
nx.draw(G, with_labels=True)

plt.title("Simple Graph Visualization", fontsize=14)
plt.show()