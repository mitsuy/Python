import cv2
import numpy as np
import matplotlib.pyplot as plt

# read picture with grayscale
img=cv2.imread('test.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

tmp=cv2.imread('temp.jpg')
tmp=cv2.cvtColor(tmp,cv2.COLOR_BGR2RGB)

width,height,ch=tmp.shape
#width,height=tmp.shape[::-1]

# All the 6 methods
methods=['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED',
         'cv2.TM_CCORR','cv2.TM_CCORR_NORMED',
         'cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']


for m in methods:
    img_cp=img.copy()
    method=eval(m)

    # Apply template Matching
    res=cv2.matchTemplate(img_cp,tmp,method)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED,
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left=min_loc
    else:
        top_left=max_loc
    # end if
    
    bottom_right=(top_left[0]+width,top_left[1]+height)

    cv2.rectangle(img_cp,top_left,bottom_right,(255,0,0),2)
    cv2.imwrite('res.png',img_cp)
    
    plt.subplot(121)
    plt.imshow(res)
    plt.title('Matching result')

    plt.subplot(122)
    plt.imshow(img_cp)
    plt.title('Detected Point')

    plt.show()
# end for
