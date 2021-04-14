# State: works 
# ToDo: needs adjustment for 'images'
'''
Imports:
'''
import cv2
import numpy as np
import variables as v

'''
Code:
'''
def get_contours(img, drawContour, gray, blur, canny): # img only takes canny images originating from gray color model, additionaly only uses the latest 4 arguments for showcasing
    
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours: # cnt represents contour values
        area = cv2.contourArea(cnt)
        #print(area) # maybe use values to cut to edges?
        
        if  60 > area > 15 : # adjust for needed object size
            cv2.drawContours(drawContour, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt, True) # get contour parameter
            #print(peri)

            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) # adjust here for image
            #print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3: objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.98 and aspRatio < 1.03: objectType = "Square"
                else: objectType = "Rectangle"
            elif objCor > 4: objectType = "Circles"
            else: objectType = "None"

            cv2.rectangle(drawContour, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(drawContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)
            
            image_stacked = v.stackImages(0.8, ([v.image_int, gray, blur],
                                                [canny, drawContour, v.image_blank]))

            image_resized = cv2.resize(image_stacked, (1200, 400)) # function to resize image                               

    cv2.imshow("Stacked", image_resized)
    cv2.waitKey(0)

# Show
get_contours(v.image_canny1, v.image_cp1, v.image_gray1, v.image_gaussian1, v.image_canny1)


