import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10,4), columns=["A","B","C","D"])

fig, ax = plt.subplots()
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

for i in range(len(df)):
    for j in range(len(df.columns)):
        value = df.iloc[i, j]
        if value < 0:
            table[(i+1, j)].get_text().set_color('red')
        else:
            table[(i+1, j)].get_text().set_color('black')

plt.show()
