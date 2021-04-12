#State: works but coords are cluttered
'''
Imports:
'''
import cv2
import numpy as np
import variables as v

'''
Function:
'''
def get_contours(img):

    _, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)   

    for cnt in contours: # cnt represents contour values
        area = cv2.contourArea(cnt)
        #print(area) # maybe use values to cut to edges? 
        
        if 60 > area > 15: # adjust for needed object size
            cv2.drawContours(img_contour, cnt, -1, (255,0,0), 3) # cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)
            peri = cv2.arcLength(cnt, True) # get contour parameter
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) # adjust here for image
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
                        (x+(w//2)-10,y+(h//2)-10),font,0.5,
                        (0,0,0),2)
            
            n = approx.ravel() # Used to flatten the array containing the co-ordinates of the vertices
            i = 0
  
            for j in n :
                if(i % 2 == 0):
                    x = n[i]
                    y = n[i + 1]
        
                    # String containing the co-ordinates.
                    string = str(x) + " " + str(y) 
        
                    if(i == 0):
                        # text on topmost co-ordinate.
                        cv2.putText(img_contour, "Arrow tip", (x, y),
                                        font, 0.5, (255, 0, 0)) 
                    else:
                        # text on remaining co-ordinates.
                        cv2.putText(img_contour, string, (x, y), 
                                font, 0.5, (255, 255, 255)) 
                i = i + 1

'''
File specific variables:
'''
font = cv2.FONT_HERSHEY_COMPLEX

img = v.image
img_contour = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7),1)
img_canny = cv2.Canny(img_blur,50,50)

get_contours(img_canny)

img_blank = np.zeros_like(img)

img_stacked = v.stackImages(0.8, ([img, img_gray, img_blur],
                                [img_canny, img_contour, img_blank]))

cv2.imshow("Stacked", img_stacked)
cv2.waitKey(0)