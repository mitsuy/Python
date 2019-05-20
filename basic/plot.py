import matplotlib.pyplot as plt
import numpy as np


# Generation of data
x=np.linspace(0,10,100)
y=np.sin(x)+np.random.randn(100)

y2=0.0001*np.exp(x)+np.random.randn(100)




# Plot

# Use Tex 
#plt.rc('text',usetex=True)
#plt.rc('font',family='serif')

fig=plt.plot(x,y,label="test")
fig2=plt.plot(x,y2,label="e^x")

plt.title("$\sin(x)+random$ and $e^{x}+random$")
plt.show()
