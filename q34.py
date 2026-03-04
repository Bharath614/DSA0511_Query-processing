import numpy as np
import matplotlib.pyplot as plt

x=np.random.rand(50)
y=np.random.rand(50)
sizes=np.random.rand(50)*1000

plt.scatter(x,y,s=sizes)
plt.show()
