#####################################################
#
#  How to use Fast Fourier Transformation liblary.
#
#  Make time-frequency data and output to file.
#  read data of file which makes by myself and do FFT.
#
#
#  Written by M.YAGYU, 21 May 2019
#
#####################################################



import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

def main():
    # paramters of data
    N=256                           # Sampling number
    delt=0.01                       # sampling width
    f1=5                            # frequencies
    f2=40                           # frequencies
    omega1=f1*2*np.pi               
    omega2=f2*2*np.pi
    
    t=np.arange(0,N*delt,delt)      # time pivot
    freq=np.linspace(0,1./delt,N)   # freq. pivot


    # Generate signal
    f=np.sin(omega1*t)+0.2*np.sin(omega2*t)
    
    # Stored t and f to tmp (as 2D aray)
    tmp=np.c_[t,f]
       
    # Output to file
    np.savetxt('test_data.dat',tmp,fmt='%5.2e',delimiter='\t')
    
    # Read file and store data
    data=np.loadtxt("test_data.dat",delimiter='\t',comments='#')
    t1=data[:,0]
    f1=data[:,1]
    '''
    i,j=0,0
    t1=np.zeros(N)
    f1=np.zeros(N)
    for i in range(0,2):
        for j in range(N):
            if i == 0:
                t1[j]=data[j][i]
            else:
                f1[j]=data[j][i]

    '''
    
    # Fast Fourier Transformation
    F=np.fft.fft(f1)

    # Save data after FFT
    np.savetxt("test_fft.dat",F,fmt='%5.3f')
    
    # Calculating amplitude spectrum
    amp=np.abs(F)

    # Plot
    plt.figure()
    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['font.size']='17'
    plt.subplot(121)
    plt.plot(t1,f1,label='f(t)',color="red")
    plt.xlabel("Time",fontsize=20)
    plt.ylabel("Signal",fontsize=20)
    plt.grid()
    leg=plt.legend(loc=1,fontsize=25)
    leg.get_frame().set_alpha(1)

    plt.subplot(122)
    plt.plot(freq,amp,label='|F(k)|',color="red")
    plt.xlabel("Frequency",fontsize=20)
    plt.ylabel("Spectrum",fontsize=20)
    plt.grid()
    leg=plt.legend(loc=1,fontsize=25)
    leg.get_frame().set_alpha(1)
    plt.savefig('fft.png')
    plt.show()

#end main
    
if __name__ =="__main__":
    main()
