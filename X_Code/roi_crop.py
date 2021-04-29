# State: works
# ToDo: works only on squares/rectangles and specific sizes atm
'''
Imports:
'''
import cv2
import numpy as np
import variables as v
from matplotlib import pyplot as plt

'''
Code:
'''
def crop(img, gray, blur):

    # threshold and morph-close-op
    retval, threshed = cv2.threshold(blur, 110, 255, cv2.THRESH_BINARY_INV)
    closed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, v.kernel2)

    # project to the axis
    H,W = img.shape[:2]
    xx = np.sum(closed, axis=0)/H
    yy = np.sum(closed, axis=1)/W

    # threshold and find the nozero
    xx[xx<60] = 0
    yy[yy<100] = 0

    ixx = xx.nonzero()
    iyy = yy.nonzero()
    x1,x2 = ixx[0][0], ixx[0][-1]
    y1,y2 = iyy[0][0], iyy[0][-1]

    # label on the original image and save it.
    lined = cv2.rectangle(img.copy(), (x1,y1),(x2,y2), (0,0,255),2)
    cropped = img[y1:y2,x1:x2]

    cv2.imshow("Lined.png", lined)
    cv2.imshow("Cropped.png", cropped)
    cv2.waitKey(0)

crop(v.image_int, v.image_gray1, v.image_median1)