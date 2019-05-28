import sys
import numpy as np



def write_data(t,f,ff,freq,spc,spc2,args):

    ### Make up all data into a array "data_all"
    data_all=np.c_[t,f,ff,freq,spc,spc2]
    data_str="# time           Signal       Signal_ifft        freq.         spc_fft        spc_noise_cancel"


    ### Output data_all to file
    np.savetxt('data/'+args[2],data_all,fmt='%8.3f',delimiter='\t'\
               ,header=data_str,comments='#')

    
## end write_data
