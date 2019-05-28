import numpy as np


def fft(f):
    
    F=np.fft.fft(f)
    spc=np.abs(F)    # Spectrum

    return F,spc

##end fft

def ifft(fc,FF,freq):

    ### Low-pass filter (LPF)
    FF[(freq>fc)]=0
    spc2=np.abs(FF)
    
    ### IFFT
    ff=np.fft.ifft(FF)
    #ff=np.real(ff*N)   ### return to original scale.

    return FF,spc2,ff

##end ifft
