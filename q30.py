import numpy as np
import matplotlib.pyplot as plt

men=(22,30,35,35,26)
women=(25,32,30,35,29)

x=np.arange(len(men))
width=0.35

plt.bar(x-width/2,men,width)
plt.bar(x+width/2,women,width)
plt.show()
