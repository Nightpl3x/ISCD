import cv2
import numpy as np
import variables as v

def empty(a):
    pass

def stackImages(scale,imgArray): # copy paste function to stack images
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)

cv2.createTrackbar("Hue Min", "Trackbars",59,179,empty) # set arg1 to 0
cv2.createTrackbar("Hue Max", "Trackbars",115,179,empty) # set arg1 to 179
cv2.createTrackbar("Sat Min", "Trackbars",0,255,empty) # set arg1 to 0
cv2.createTrackbar("Sat Max", "Trackbars",58,255,empty) # set arg1 to 255
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
    image_mask = cv2.inRange(v.image_copy, lower, upper)
    image_result = cv2.bitwise_and(v.image_copy, v.image_copy, mask = image_mask)

    # Show images stacked
    images_stacked = stackImages(0.6, ([v.image_copy, v.image_HSV], [image_mask, image_result]))
    cv2.imshow("Stacked Images", images_stacked)

    cv2.waitKey(1)