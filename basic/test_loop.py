######################################################################################
#                                                                                    #
#  Test of Loop calculation.                                                         #
#                                                                                    #
#  How to play:                                                                      #
#   Choose '1' or '2'.                                                               #
#   If choose '1', can input integer number n to calculate summation 1+2+...+n .     #
#   If choose '2', can input integer number n to show n*n multiplication table.      #
#   If not do them, you can try to choose their numbers again but if you make a      #
#   mistake many times, have to execute again.                                       #
#                                                                                    #
#                                                                                    #
#  Written by M.Yagyu, 15 May 2019                                                   #
#                                                                                    #
#                                                                                    #
######################################################################################


# program test_loop

k=0     # int
loop=2  # int

while k<loop:
    ch=input('Please choose 1 or 2 and push Enter : ')  # char
        
    if ch =='1':

        ###
        ###  SUMMATION
        ###
        
        tmp=0     # Initilization,int

        iter=input('\n\n 1+2+3+.....+n\n n=')   # char
        iter=int(iter)  # int

        for i in range(iter+1):   # i:int
            tmp+=i
        #end for

        print('\n\n Summation')
        print("1+2+....+",iter,'=',tmp,'\n')
        break
    
        ###
        ### END SUMMATION
        ###

    elif ch =='2':

        ### 
        ### MULTIPLICATION TABLE
        ###
        it=input('Input any number n > 1 : ')   # char
        it=int(it)  # int

        for i in range(it):
            for j in range(it):
                mult=(i+1)*(j+1)   # int
                print('%5d' %mult,end="")
                #print('{1}'.format(mult),end="")
            #end for
            print("")

        #end for
        break
    
        ###
        ### END MULTIPLICATION TABLE
        ###
        
    else:
        
        ###
        ### EXCEPTION HANDLING
        ###
        
        if k<(loop-1):
            print('\n\n Please choose 1 or 2 !!!!\n\n')
        else:
            print('\n\nEXECUTE AGAIN !!\n\n')

        ###
        ### END EXCEPTION HANDLING
        ###
        
    k+=1
#end while

# end program test_loop
