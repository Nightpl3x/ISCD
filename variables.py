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
image = cv2.imread('images/S2_Kovacs_10000Z.jpeg', cv2.IMREAD_COLOR) # :Workplace relative path
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # convert to rgb


'''
Image processing variables:
'''
image_copy = np.copy(image) # copying the image so we dont alter the original

image_gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY) # turn rgb image into a grayed version 

image_HSV = cv2.cvtColor(image_copy, cv2.COLOR_RGB2HSV) # create image in hsv for the color schemes extraction
                                    
#                                   low , high threshold 
image_edges = cv2.Canny(image_copy, 100 , 150) # makes edges more visible, used for the Hough transform in edges_lined()

'''
Kernels: https://en.wikipedia.org/wiki/Kernel_(image_processing)
'''
kernel = np.ones((5,5), np.uint8) # 5x5 Einheitsmatrix
kernel2 = np.ones((7,7), np.uint8) # 7x7 Einheitsmatrix

kernel3 = np.array(([0, 1, 0],
					[1, 1, 1],
					[0, 1, 0]),dtype='uint8') # Wikipedia Test Matrix

kernel_sharp = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) 

image_kernel = cv2.filter2D(image_copy, -1, kernel) # 'enhance' image via kernels (image variable is for testing only)

'''
Unused image processing variables:
'''
image_blur = cv2.medianBlur(image_copy, 5) # Blur image to reduce noise(5 indicates the level of blurring)

image_resized = cv2.resize(image, (1200, 600)) # function to resize image, if ever needed

