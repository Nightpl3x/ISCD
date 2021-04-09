'''
Imports:
'''
import cv2
import numpy as np

def stackImages(scale,imgArray):
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

def get_contours(img):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours: # cnt represents contour values
        area = cv2.contourArea(cnt)
        # print(area) # maybe use values to cut to edges?
        
        if 60 > area > 15: # adjust for needed object size
            cv2.drawContours(img_contour, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt, True) # get contour parameter
            approx = cv2.approxPolyDP(cnt, 0.01*peri, True) #adjust here for image
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3: objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4: objectType = "Circles"
            else: objectType = "None"

            cv2.rectangle(img_contour, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img_contour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)

'''
File specific variables:
'''
#path_shapes = "images_testing/shapes.png"
path_shapes = "images_testing\ErodeDilateOpen.png"

img = cv2.imread(path_shapes)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # convert to rgb
img_contour = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7),1)
img_canny = cv2.Canny(img_blur,50,50)
get_contours(img_canny)

img_blank = np.zeros_like(img)
img_stacked = stackImages(0.8, ([img, img_gray, img_blur],
                                [img_canny, img_contour, img_blank]))

cv2.imshow("Stacked", img_stacked)
cv2.waitKey(0)