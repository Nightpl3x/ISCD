# State: works
# ToDo: Code cleanup maybe

'''
Imports:
'''
import cv2
import numpy as np
import variables as v

'''
Functions:
'''
def empty(a):
    pass

'''
Setup Trackbars:
'''
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)

cv2.createTrackbar("Hue Min", "Trackbars",0,179,empty) # set arg1 to 0
cv2.createTrackbar("Hue Max", "Trackbars",179,179,empty) # set arg1 to 179
cv2.createTrackbar("Sat Min", "Trackbars",0,255,empty) # set arg1 to 0
cv2.createTrackbar("Sat Max", "Trackbars",255,255,empty) # set arg1 to 255
cv2.createTrackbar("Val Min", "Trackbars",0,255,empty) # set arg1 to 0
cv2.createTrackbar("Val Max", "Trackbars",255,255,empty) # set arg1 to 255

while True:

    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    image_mask = cv2.inRange(v.image_int, lower, upper)
    image_result = cv2.bitwise_and(v.image_int, v.image_int, mask = image_mask)

    # Show images stacked
    images_stacked = v.stackImages(0.6, ([v.image_int, v.image_HSV1], [image_mask, image_result]))
    cv2.imshow("Stacked Images", images_stacked)

    cv2.waitKey(1)