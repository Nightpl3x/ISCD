from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
image selection
'''
image = cv2.imread('images\S2_Kovacs_10000Z.jpeg') # :Workplace relative path

'''
image processing variables
'''
# read images via the image path (Important: Only use the pah of your current device and comment the other out!)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #convert to rgb just to be safe later on
image_copy = np.copy(image) #copying the image so we dont alter the original
image_copy_HSV = cv2.cvtColor(image_copy, cv2.COLOR_RGB2HSV) #create a copy to test hsv

'''
Edge detection specific variables
'''
low_threshold = 80
high_threshold = 140
image_edges = cv2.Canny(image_copy, low_threshold, high_threshold)
    