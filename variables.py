import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
image selection
'''
image = cv2.imread('images/20H_10000Z.jpeg') # :Workplace relative path

'''
num variables
'''
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) # to sharpen image

low_threshold = 100 # for image edge detection
high_threshold = 150 # for image edge detection

'''
image processing variables
'''
# read images via the image path (Important: Only use the pah of your current device and comment the other out!)

image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #convert to rgb just to be safe later on

image_copy = np.copy(image) #copying the image so we dont alter the original

image_gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

image_blur = cv2.filter2D(image_copy, -1, sharpen_kernel) # enhance image https://stackoverflow.com/questions/58231849/how-to-remove-blurriness-from-an-image-using-opencv-python-c

image_blur_gray = cv2.filter2D(image_gray, -1, sharpen_kernel) # enhance image_gray

image_HSV = cv2.cvtColor(image_copy, cv2.COLOR_RGB2HSV) #create a copy to test hsv

image_edges = cv2.Canny(image_copy, low_threshold, high_threshold, None, 3)
    