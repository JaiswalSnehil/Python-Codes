import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = np.random.rand(100, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

sns.pairplot(df)
plt.show()