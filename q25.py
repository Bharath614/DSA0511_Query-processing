import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[10,20,30,40,50]
y2=[5,15,25,35,45]

plt.plot(x,y1,label="Line1",linewidth=2,color="blue")
plt.plot(x,y2,label="Line2",linewidth=4,color="red")
plt.legend()
plt.show()
