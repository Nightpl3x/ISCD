import cv2
import numpy as np
import matplotlib.pyplot as plt
import variables as v

img = v.image_copy

def image_enhance(): # enhance coloration via CLAHE (variables: all )

    # https://stackoverflow.com/questions/25008458/how-to-apply-clahe-on-rgb-color-images

    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8)) # determine CLAHE paramters (values based on recommendations)

    image_lab = cv2.cvtColor(v.image_copy, cv2.COLOR_RGB2LAB)  # convert from RGB to LAB, change v.image_copy here to view other images
    
    l, a, b = cv2.split(image_lab)  # split on 3 different channels

    l2 = clahe.apply(l)  # apply CLAHE to the L-channel

    image_lab = cv2.merge((l2,a,b))  # merge channels with the altered 'l' version
    image_enhanced = cv2.cvtColor(image_lab, cv2.COLOR_LAB2RGB)  # convert from LAB back to RGB
    global image_edges_enhanced 
    image_edges_enhanced = cv2.Canny(image_enhanced, 100, 150) # makes edges more visible, used for the Hough transform in edges_lined()

    circle_detection(image_edges_enhanced)

def circle_detection(image_edges_enhanced): # detect circles via Hough transform (variables: image_edges, all )

    # https://learnopencv.com/hough-transform-with-opencv-c-python/amp/

    image_circles = cv2.HoughCircles(image_edges_enhanced, cv2.HOUGH_GRADIENT, 1, 20, param1=20, param2=10, minRadius=25, maxRadius=35) # Apply Hough transform on the image

    if image_circles is not None: # Draw detected circles
        image_circles = np.uint16(np.around(image_circles))
        for i in image_circles[0, :]:
            
            cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 5) # Draw outer circle
        
            cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 3) # Draw inner circle

        black_out(img)

def black_out(img): # remove white space via HSV (variables: image_HSV, all )

    lower_Hue = np.array([160,0,0])
    high_Hue = np.array([180,255,255])

    image_HSV_test = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask_HSV = cv2.inRange(image_HSV_test, lower_Hue, high_Hue)

    image_HSV_test = np.copy(img) # change here for other images

    image_HSV_test[mask_HSV == 0] = [0,0,0]

    plt.imshow(image_HSV_test)
    plt.show()

image_enhance()