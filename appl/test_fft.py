#####################################################
#
#  How to use Fast Fourier Translation liblary.
#
#
#
#  Written by M.YAGYU, 21 May 2019
#
#####################################################



import numpy as np
import matplotlib.pyplot as plt


# paramters of data
N=256                           # Sampling number
delt=0.01                       # sampling width
f1=50                           # frequencies
f2=60                           # frequencies
omega1=f1*2*np.pi               
omega2=f2*2*np.pi

t=np.arange(0,N*delt,delt)      # time pivot
freq=np.linspace(0,1./delt,N)   # freq. pivot


# generating signal
#f=np.sin(omega1*t)+np.sin(omega2*t)+0.3*np.random.randn(N)
f=np.sqrt(2.)*np.sin(omega1*t)


n=25
fn=0.
for i in range(1,n,2):
    fn=(1/i)*np.sqrt(2.)*np.sin(i*omega1*t)+fn
#end for
f=f+fn

# Fast Fourier Translation
F=np.fft.fft(f)

# Calculating amplitude spectrum
amp=np.abs(F)


# Plot
plt.figure()
plt.rcParams['font.family']='Times New Roman'
plt.rcParams['font.size']='17'
plt.subplot(121)
plt.plot(t,f,label='f(n)',color="red")
plt.xlabel("Time",fontsize=20)
plt.ylabel("Signal",fontsize=20)
plt.grid()
leg=plt.legend(loc=1,fontsize=25)
leg.get_frame().set_alpha(1)
plt.subplot(122)

plt.plot(freq,amp,label='|F(k)|',color="red")
plt.xlabel("Frequency",fontsize=20)
plt.ylabel("Amplitude",fontsize=20)
plt.grid()
leg=plt.legend(loc=1,fontsize=25)
leg.get_frame().set_alpha(1)
plt.show()

