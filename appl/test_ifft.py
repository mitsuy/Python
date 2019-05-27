###############################################################################
#
#  Inverse Fast Fourier Transformation (IFFT).
# 
#  Read data done FFT from file "test_fft.dat", then the data
#  is processed by Low-Pass-Filter. The processed data finally
#  is done IFFT.
#
#  Kind of data file:
#    test_data.dat : Time-series data for signal
#    test_fft.dat  : Data of freq vs Spectrum, which is done FFT
#    test_ifft.dat : Time-series data for signal, which is canceled noise.
#
#    test_fft_ifft.dat : Make up above data into a file.
#
#
#  Written by M.YAGYU, 27 May 2019
#
################################################################################


import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():

    # Read date from any datafile. 
    data=np.loadtxt("test_data.dat",dtype='float')

    # Store data to array t and f.
    t=data[:,0]      # Time
    f=data[:,1]      # Signal
    
    delt=t[1]-t[0]   # Sampling width

    # Read data done FFT as complex number
    F=np.loadtxt("test_fft.dat",dtype='complex')
    spc=np.abs(F)    # Spectrum
    
    N=len(F)         # Get data length.
    FF=F.copy()      # Copy F on FF
    
    freq=np.linspace(0,1./delt,N)  # Freq. pivot

    ########################################
    #                                      #
    #   fc is freq. for canceling noise.   #
    #                                      #
    ########################################
    fc=20                          # Cut-off frequency
    
    # Normalization and make alternative comps. twice times.
    FF=FF/(N/2)
    FF[0]=F[0]*0.5

    # Low-pass filter (LPF)
    FF[(freq>fc)]=0
    spc2=np.abs(FF)
    
    # IFFT
    ff=np.fft.ifft(FF)
    ff=np.real(ff*N)   # return to original scale.

    # Make up all data into a array "data_all"
    data_all=np.c_[t,f,ff,freq,spc,spc2]
    data_str="# time           Signal       Signal_ifft        freq.         spc_fft        spc_ifft"

    # Output data_all to file
    np.savetxt("test_fft_ifft.dat",data_all,fmt='%8.3f',delimiter='\t'\
               ,header=data_str,comments='#')


    
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
    #plt.title("Inverse Fourier Transformation",loc,fontsize=25)
    #plt.savefig('ifft.png')
    plt.show()

#end main


if __name__=='__main__':
    main()
