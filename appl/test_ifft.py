##############################################################
#
#  Inverse Fast Fourier Translation (IFFT).
# 
#  Read data done FFT from file "test_data.dat", then the data
#  is processed by Low-Pass-Filter. The processed data finally
#  is done IFFT.
#
#
#  Written by M.YAGYU, 27 May 2019
#
###############################################################


import numpy as np
import matplotlib.pyplot as plt

def main():

    # Read date from any datafile.
    data=np.loadtxt("test_data.dat",dtype='float')

    #store data to array.
    t=data[:,0]
    delt=t[1]-t[0]  # Sampling width

    # Read data done FFT as complex number
    F=np.loadtxt("test_fft.dat",dtype='complex')
    N=len(F)     # Get data number.

    
    freq=np.linspace(0,1./delt,N)  # Freq. pivot
    fc=20                          # Cut-off frequency
    
    # Normalization and make alternative comps. twice times.
    F=F/(N/2)
    F[0]=F[0]*0.5

    # Low-pass filter (LPF)
    F[(freq>fc)]=0

    # IFFT
    f=np.fft.ifft(F)
    f=np.real(f*N)   # return to  original scale.


    # Plot
    plt.figure()
    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['font.size']='17'
    plt.subplot(121)
    plt.plot(t,f,label='f(t)',color="red")
    plt.xlabel("Time",fontsize=20)
    plt.ylabel("Signal",fontsize=20)
    plt.grid()
    leg=plt.legend(loc=1,fontsize=25)
    leg.get_frame().set_alpha(1)


    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['font.size']='17'
    plt.subplot(122)
    plt.plot(freq,np.abs(F),label='|F|',color="red")
    plt.xlabel("Frequency",fontsize=20)
    plt.ylabel("Spectrum",fontsize=20)
    plt.grid()
    leg=plt.legend(loc=1,fontsize=25)
    leg.get_frame().set_alpha(1)
    plt.show()

#end main


if __name__=='__main__':
    main()
