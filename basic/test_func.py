#
#  Test Function with Python
#
#  Written by M.Yagyu, 15 May 2019
#

def test_func(val1,val2,op):

    if op == 1:
        print("Summation")
        print(val1+val2)
    elif op == 2:
        print("Difference")
        print(val1-val2)
    elif op == 3:
        print("Multiplication")
        print(val1*val2)
    elif op == 4:
        print("Devided")
        print(val1/val2)
    else:
        print("%d is Unknown operation number."%op)
    #end if
    
# end test_func


    
##############
#    Main    # 
##############
op=int(input('Choose 1,2,3 or 4 : \n'))
val1=float(input('Input any value val1= \n'))
val2=float(input('Input any value val2= \n'))

test_func(val1,val2,op)
    
