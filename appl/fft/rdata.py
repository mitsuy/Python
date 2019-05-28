import sys
import numpy as np


def data_read(args):

    ### Read Time vs Signal date from any datafile. 
    data=np.loadtxt('data/'+args[1],dtype='float')

    ### Store data to array t and f and calc delt.
    t=data[:,0]      # Time
    f=data[:,1]      # Signal
    delt=t[1]-t[0]   # Sampling width
    N=len(f)         # Get data length.
    
    freq=np.linspace(0,1./delt,N)  # Freq. pivot    

    return t,f,delt,N,freq
##data_read
