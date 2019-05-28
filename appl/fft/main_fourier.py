############################################################################################
#                                                                                          #
#                                                                                          #
#  The script for Fourier analysis of experimental data.                                   #
#                                                                                          #
#  Read data of time-series for signal, then the data is done FFT                          #
#  and processed by Low-Pass-Filter. The processed data finally is done IFFT.              #
#                                                                                          #
#                                                                                          #
#  Kind of data file:                                                                      #
#    args[1] : Time-series data for signal                                                 #
#    args[2] : Make up time, signal,noise canceled signal, spectrum and                    #
#              noise canceled spectrum into a file.                                        #
#                                                                                          #
#                                                                                          #
#  -How to executive on terminal:                                                          #
#                                                                                          #
#              $ python fft_ifft.py args[1] args[2] args[3]                                #
#                                                                                          #
#    Where args[1], args[2] and args[3] are low data file name to read,                    #
#   calculated data file name (To refer above 'Kind of data file') and                     #
#   graph name for saving,respectively. However, note that graph extension is 'png'        #
#                                                                                          #
#                                                                                          #
#  -Example of executing:                                                                  #
#                                                                                          #
#              $ python fft_ifft.py test_data.dat data_all.dat fft_ifft.png                #
#                                                                                          #
#                                                                                          #
#                                                                                          #
#                                                                                          #
#       Written by M.YAGYU, 27 May 2019                                                    #
#                                                                                          #
#       Modified :                                                                         #
#                 Minor change  by M.Yagyu 28 May 2019                                     #
#                                                                                          #
############################################################################################

### Module
import numpy as np
import matplotlib.pyplot as plt
import sys

### Function
from pldata import graph
from rdata import data_read
from fft_ifft import fft,ifft
from opdata import write_data

def main():
    args=sys.argv

    ### fc is freq. for canceling noise. 
    fc=20              # Cut-off frequency

    
    ### Read data from file ###
    t,f,delt,N,freq=data_read(args)
    
    ### Fast Fourier Transformation ###
    F,spc=fft(f)
    
    FF=F.copy()      # Copy F to FF
    
    ### Inverse Fourier Transformation ###
    FF,spc2,ff=ifft(fc,FF,freq)

    ### Output data to file ###
    write_data(t,f,ff,freq,spc,spc2,args)

    ### Plot data ###
    graph(t,f,freq,spc,ff,spc2,args)

##end main


if __name__=='__main__':
    main()
