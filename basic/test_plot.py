import matplotlib.pyplot as plt
import numpy as np


# Setting math
sin=np.sin
pi=np.pi
sq=np.sqrt

n=13
phi1=0.
I1=1.

# Generation of data
t=np.linspace(0,n*pi,n*10)
i1=sq(2.)*I1*sin(t-phi1)


I_n=I1
phi_n=0.
#i=2
i_n=0.

for i in range(1,n,2):
    i_n=sq(2.)*I_n*sin(i*t-phi_n)+i_n

#    I_n=I_n+0.1
    phi_n=phi_n+pi/2.
#end for

i=i1+i_n

# Plot
plt.xlabel('\u03B8 [rad]')
plt.ylabel('Current [A]')

fig=plt.plot(t,i1,label='i1',linestyle="dashed",linewidth=2,color="black")
fig2=plt.plot(t,i_n,label="in=\u03A3 in...,Comps.of high harmonic")
fig3=plt.plot(t,i,label="i=i1+in",color="red",linewidth=1)

plt.legend()
plt.title("")
plt.show()
