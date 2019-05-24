#####################################################
#
#  How to use Fast Fourier Translation liblary.
#
#  Make time-frequency data and output to file.
#  read data of file which makes by myself and do FFT.
#
#
#  Written by M.YAGYU, 21 May 2019
#
#####################################################



import numpy as np
import matplotlib.pyplot as plt
import sys


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

f=np.sqrt(2.)*np.sin(omega1*t)


n=25
fn=0.
for i in range(1,n,2):
    fn=(1/i)*np.sqrt(2.)*np.sin(i*omega1*t)+fn
#end for
f=f+fn

# Output to file
fp=open('test_data.dat','w')
for j in range(int(N)):
    
    fp.write(str(t[j]))
    fp.write('\t')
    fp.write(str(f[j]))
    fp.write('\n')
fp.close()

#fp=open('test_data.dat','r')
#line=fp.readlines()
#fp.close()
#print (line)

# Read file and store data
data=np.loadtxt("test_data.dat",delimiter='\t',comments='#')

i,j=0,0
t1=np.zeros(N)
f1=np.zeros(N)
for i in range(0,2):
    for j in range(N):
        if i == 0:
            t1[j]=data[j][i]
        else:
            f1[j]=data[j][i]


# Fast Fourier Translation
F=np.fft.fft(f1)

# Calculating amplitude spectrum
amp=np.abs(F)


# Plot
plt.figure()
plt.rcParams['font.family']='Times New Roman'
plt.rcParams['font.size']='17'
plt.subplot(121)
plt.plot(t1,f1,label='f(n)',color="red")
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

