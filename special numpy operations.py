import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
#print(plt.plot(x,y))
#plt.show()#This will plot the graphs for x and y
z=np.cos(x)
#plt.plot(x,z)
#plt.show()
v=np.tan(x)
plt.plot(x,v)
plt.show()

