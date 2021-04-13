#State: works only on squares/rectangles
'''
Imports:
'''
import cv2
import numpy as np
import variables as v
from matplotlib import pyplot as plt
import time

'''
Code:
'''
img = v.image_int
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## medianBlur, threshold and morph-close-op
median = cv2.medianBlur(gray, ksize=17)
retval, threshed = cv2.threshold(median, 110, 255, cv2.THRESH_BINARY_INV)
closed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, v.kernel2)

## Project to the axis
H,W = img.shape[:2]
xx = np.sum(closed, axis=0)/H
yy = np.sum(closed, axis=1)/W

## Threshold and find the nozero
xx[xx<60] = 0
yy[yy<100] = 0

ixx = xx.nonzero()
iyy = yy.nonzero()
x1,x2 = ixx[0][0], ixx[0][-1]
y1,y2 = iyy[0][0], iyy[0][-1]

## label on the original image and save it.
res1 = cv2.rectangle(img.copy(), (x1,y1),(x2,y2), (0,0,255),2)
res2 = img[y1:y2,x1:x2]

cv2.imshow("result1.png", res1)
cv2.imshow("result2.png", res2)
cv2.waitKey(0)