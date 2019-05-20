#
# Exception handling test
#
#
# Written by M.Yagyu, 15 May 2019
#



##
##  exception func
##
def exception_test(val1,val2):
    print( "\n--- Start calc. ! ---\n")

    result=0.   #real

    try:
        result=val1*val2
    except:
        print("\n Cant calculate.\n")
        raise
    finally:
        print("\nfinish calc.\n")

    return result


###
###  Main func
###

try:
    print(exception_test(1.5,200))
    print(exception_test(4.5,'45'))
except:
    print("Found error!!")
