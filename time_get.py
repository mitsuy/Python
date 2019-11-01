import datetime
import sys

def main():

    ### Init. ###
    sec=0
    dammy=1
    cnt=0

    while 1:
        dt_now=datetime.datetime.now()  # get current time and date
        sec=dt_now.second               # get current time [sec]
        
        if sec != dammy: 

            if cnt !=0:
                print('{ten} [sec]  {sixteen}'
                      .format(ten=cnt,sixteen=hex(cnt)))

            #end if

            if cnt == 5:
                '''
                write some handling here.
                '''
                break
            #end if
            
            cnt+=1
            
        #end if
        
        dammy=sec
        
    #end while
    
#end main


if __name__=='__main__':
    main()
