import networkx as nx
import random
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(40,0.05)
state = {n: random.random() for n in G.nodes()}

for _ in range(10):
    for n in G.nodes():
        state[n] = sum(state.get(m,0)
    for m in G.neighbors(n))/max(1,len(list(G.neighbors(n))))
        
colors = [state[n] for n in G.nodes()]
nx.draw(G, node_color=colors, cmap="coolwarm")
plt.title("Thought Diffusion")
plt.show()