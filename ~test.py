import cv2
import numpy as np
import matplotlib.pyplot as plt
import variables as v

image_circles = cv2.HoughCircles(v.image_edges, cv2.HOUGH_GRADIENT, 1, 20, param1=20, param2=10, minRadius=25, maxRadius=35) # Apply Hough transform on the image

if image_circles is not None: # Draw detected circles
    image_circles = np.uint16(np.around(image_circles))
    for i in image_circles[0, :]:
        
        cv2.circle(v.image_copy, (i[0], i[1]), i[2], (0, 0, 255), 1) # Draw outer circle
       
        cv2.circle(v.image_copy, (i[0], i[1]), 2, (255, 0, 0), 1) # Draw inner circle

plt.imshow(v.image_copy)
plt.show()

# https://learnopencv.com/hough-transform-with-opencv-c-python/amp/
# https://www.geeksforgeeks.org/circle-detection-using-opencv-python/