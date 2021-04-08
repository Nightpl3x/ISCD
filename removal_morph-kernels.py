import cv2
import numpy as np
import variables as v

img = v.image_copy
'''
Kernels:
'''
kernel = np.ones((5,5), np.uint8) # 5x5 Einheitsmatrix
kernel2 = np.ones((7,7), np.uint8) # 7x7 Einheitsmatrix
kernel3 = np.array(([0, 1, 0],
					[1, 1, 1],
					[0, 1, 0]),dtype='uint8') # Wikipedia Test Matrix

'''
Basic modification:
'''
img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

img_openXclose = cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel)

'''
Advanced modification:
'''
img_erode = cv2.erode(img, kernel3, iterations=1)
img_dilate = cv2.dilate(img_erode, kernel3, iterations=1)

img_close2 = cv2.morphologyEx(img_dilate, cv2.MORPH_CLOSE, kernel2)

img_open2 = cv2.morphologyEx(img_dilate, cv2.MORPH_OPEN, kernel2)
img_open3 = cv2.morphologyEx(img_close2, cv2.MORPH_OPEN, kernel3)

'''
Show:
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
 

'''
cv2.imwrite('Input.png', img) 
cv2.imwrite('Opening.png', img_open)
cv2.imwrite('Closing.png', img_close)
cv2.imwrite('ErosionPlusDilation.png', img_dilate)
cv2.imwrite('ErodeDilateClose.png',img_close2)
cv2.imwrite('Processed.png',img_close2)
cv2.imwrite('Final-ComparisionImage.png', img2) 
cv2.imwrite('Improved.png', close) 
'''

cv2.waitKey(0)
cv2.destroyAllWindows()