import cv2
import numpy as np
'''
Virtual Environment:
'''
#   .\env\Scripts\activate
#   deactivate

'''
Image selection:
'''
image = cv2.imread('images/28H_10000Z.jpeg', cv2.IMREAD_COLOR) # :Workplace relative path
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # convert to rgb

'''
Num variables:
'''
# opencv color codes
blue_light = (130,30,255) # HSV Color Model
blue_dark = (130,100,255) # HSV Color Model
purple_light = (140,50,150) # HSV Color Model
purple_dark = (160,200,50) # HSV Color Model
white_light = (0, 50, 200) # for images_testing
white_dark = (145, 60, 255) # for images_testing

# more kernels here: https://en.wikipedia.org/wiki/Kernel_(image_processing)
kernel_sharp = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) 

# for image edge detection
low_threshold = 100
high_threshold = 150

'''
Image processing variables:
'''
image_copy = np.copy(image) # copying the image so we dont alter the original

image_gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY) # turn rgb image into a grayed version 

image_HSV = cv2.cvtColor(image_copy, cv2.COLOR_RGB2HSV) # create image in hsv for the color schemes extraction

image_edges = cv2.Canny(image_copy, low_threshold, high_threshold) # makes edges more visible, used for the Hough transform in edges_lined()

'''
Unused variables:
'''
image_blur = cv2.medianBlur(image_copy, 5) # Blur image to reduce noise(5 indicates the level of blurring)

image_sharp = cv2.filter2D(image_copy, -1, kernel_sharp) # 'enhance' image, doesnt work well with color schemes

