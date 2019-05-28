import matplotlib.pyplot as plt
import sys

def graph(t,f,freq,spc,ff,spc2,args):
    
    ### Plot
    plt.figure(figsize=(15,8))  #(width,height)

    ### Plotting Low signal for time-series including noise
    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['font.size']='17'
    plt.subplot(221)
    plt.plot(t,f,label='f(t)',color="red")
    #plt.xlabel("Time",fontsize=20)
    plt.ylabel("Signal",fontsize=20)
    plt.grid()
    leg=plt.legend(loc=1,fontsize=25)
    leg.get_frame().set_alpha(1)

    ### Plotting spectrum including noise, which is done FFT
    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['font.size']='17'
    plt.subplot(222)
    plt.plot(freq,spc,label='|F|_fft',color="red")
    #plt.xlabel("Frequency",fontsize=20)
    plt.ylabel("Spectrum",fontsize=20)
    plt.grid()
    leg=plt.legend(loc=1,fontsize=25)
    leg.get_frame().set_alpha(1)
    #plt.title("Inverse Fourier Transformation",loc,fontsize=25)
    #plt.savefig('ifft.png')
    #plt.show()

    
    ### Plotting noise canceled signal for time-series
    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['font.size']='17'
    plt.subplot(223)
    plt.plot(t,ff,label='f(t)_ifft',color="b")
    plt.xlabel("Time",fontsize=20)
    plt.ylabel("Signal",fontsize=20)
    plt.grid()
    leg=plt.legend(loc=1,fontsize=25)
    leg.get_frame().set_alpha(1)

    ### Plotting noise canceled spectrum
    plt.rcParams['font.family']='Times New Roman'
    plt.rcParams['font.size']='17'
    plt.subplot(224)
    plt.plot(freq,spc2,label='|F|_ifft',color="b")
    plt.xlabel("Frequency",fontsize=20)
    plt.ylabel("Spectrum",fontsize=20)
    plt.grid()
    leg=plt.legend(loc=1,fontsize=25)
    leg.get_frame().set_alpha(1)
    #plt.title("Inverse Fourier Transformation",loc,fontsize=25)
    plt.savefig('graph/'+args[3])
    plt.show()
##end graph
