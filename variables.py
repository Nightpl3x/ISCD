import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Image selection:
'''
image = cv2.imread('images/20H_10000Z.jpeg') # :Workplace relative path

'''
Num variables:
'''
# more kernels here: https://en.wikipedia.org/wiki/Kernel_(image_processing)
kernel_sharp = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) 

# for image edge detection
low_threshold = 100
high_threshold = 150

'''
Image processing variables:
'''

image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #convert to rgb just to be safe later on

image_copy = np.copy(image) #copying the image so we dont alter the original

image_gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

image_sharp = cv2.filter2D(image_copy, -1, kernel_sharp) # 'enhance' image, doesnt work well with color schemes

image_HSV = cv2.cvtColor(image_copy, cv2.COLOR_RGB2HSV) #create a copy to test hsv

image_edges = cv2.Canny(image_copy, low_threshold, high_threshold, None, 3)
