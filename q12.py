import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10,4), columns=["A","B","C","D"])

fig, ax = plt.subplots()
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

for key, cell in table.get_celld().items():
    cell.set_facecolor('black')
    cell.get_text().set_color('yellow')

plt.show()
