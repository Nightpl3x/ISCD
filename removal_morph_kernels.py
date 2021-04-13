#State: works
''' 
Imports:
'''
import cv2
import numpy as np
import variables as v

img = v.image_int

'''
Basic modification:
'''
img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, v.kernel)
img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, v.kernel)

img_openXclose = cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, v.kernel)

'''
Advanced modification:
'''
img_erode = cv2.erode(img, v.kernel3, iterations=1)
img_dilate = cv2.dilate(img_erode, v.kernel3, iterations=1)

img_close2 = cv2.morphologyEx(img_dilate, cv2.MORPH_CLOSE, v.kernel2)

img_open2 = cv2.morphologyEx(img_dilate, cv2.MORPH_OPEN, v.kernel2)
img_open3 = cv2.morphologyEx(img_close2, cv2.MORPH_OPEN, v.kernel3)

'''
Show: maybe use imagesStacked()
'''
# Basics:
cv2.imshow('Input', img) 
cv2.imshow('Close', img_close)
cv2.imshow('Open', img_open)

cv2.imshow('Open + Close', img_openXclose)

# Advanced:
cv2.imshow('Erode + Dilate', img_dilate)

cv2.imshow('Erode + Dilate + Close',img_close2)

cv2.imshow('Erode + Dilate + Open',img_open2) 

cv2.imshow('Erode + Dilate + Close + Open',img_open3) 
 


#cv2.imwrite('Input.png', img)
#cv2.imwrite('Close.png', img_close)
#cv2.imwrite('Open.png', img_open)
#cv2.imwrite('ErodeDilate.png', img_dilate)
#cv2.imwrite('ErodeDilateClose.png',img_close2)
#cv2.imwrite('ErodeDilateOpen.png',img_open2)
#cv2.imwrite('ErodeDilateCloseOpen.png', img_open3) 


cv2.waitKey(0)
cv2.destroyAllWindows()