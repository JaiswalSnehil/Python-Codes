import matplotlib.pyplot as plt
import numpy as np

p = 78

fig, ax = plt.subplots(figsize=(4,4))
ax.set_facecolor('black')
t = np.linspace(0, 2*np.pi, 300)
ax.plot(np.cos(t), np.sin(t), color='grey', lw=8, alpha=0.3)

a = np.linspace(0, p/100*2*np.pi, 200)
for i in range(len(a)-1):
    ax.plot([np.cos(a[i]), np.cos(a[i+1])],
            [np.sin(a[i]), np.sin(a[i+1])],
            color=(1, i/len(a), 0), lw=0)
ax.text(0,0,f"{p}%", color='white', ha='center', va='center', fontsize=20)
ax.add_patch(plt.Circle((0,0), 0.6, color='black'))
ax.set_aspect('equal')
plt.axis('off')
plt.title('Power Ring', color='white')
plt.show()