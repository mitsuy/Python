import numpy as np
import cmath
import random
import matplotlib.pyplot as plt

pi=cmath.pi
dx=0.1

x=np.linspace(0.,2.*pi,100)

#amp
a=2.
#phase
phi=pi
#freq
f=2.
omega=2.*pi*f  

y1=np.sin(f*x)+random
y2=a*np.sin(f*x+phi)

y=y1
plt.plot(x,y)
plt.show()


#DFT
N=len(y)

X=np.zeros((N,),dtype=np.complex)
for i in range(N):
    sr,si=0,0
    for k in range(N):
        wr=np.cos(2*pi*k*i/N)
        wi=-np.sin(2*pi*k*i/N)
        sr=sr+y[k]*wr
        si=si+y[k]*wi
    X[i]=sr+si*1.j


sp=np.abs(X)
freq=np.linspace(0,1/dx,100)
plt.plot(freq,sp)
plt.show()
