#Test Branch: Enhance
#Currently working on 'Edge Detection' and 'Region of Interest'(abb.: RoI)

import cv2
import numpy as np
import matplotlib.pyplot as plt
import variables as v

'''
Functions:
'''
img = v.image_HSV

def show_image(): #shows the desired image for testing purposes
    plt.imshow(img)
    plt.show()

def show_image_gray():#only works with image_gray just a grayed version of images for testing, often better for edge detection

	plt.imshow(img, cmap='gray')
	plt.show()

def hsv_filter(): #splitting channels up in HSV color space

    #h = v.image_HSV[:,:,0] #represents the 'Hue Image Analysis' which didnt quite get us the desired results
    s = v.image_HSV[:,:,1] #represents the 'Saturation Image Analysis' which did get close to the desired results
    #v = v.image_HSV[:,:,2] #represents the 'Value Image Analysis' which didnt quite get us the desired results

    fig, (( ax1 ), ( ax2 )) = plt.subplots(2,1, figsize=(20,10)) #2 displays rows, 1 displays columns; 
    # check https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py for more information

    # Titles
    ax1.set_title('Saturation')
    ax2.set_title('Saturation_gray')

    # Images
    ax1.imshow(s)
    ax2.imshow(s, cmap='gray')

    plt.show()

def cut_out(): # Cutting out/Black out image ! needs improving, too much whitespace left

    lower_Hue = np.array([160,0,0])
    high_Hue = np.array([180,255,255])

    mask_HSV = cv2.inRange(v.image_HSV, lower_Hue, high_Hue)

    v.image_HSV = np.copy(v.image_copy)

    v.image_HSV[mask_HSV == 0] = [0,0,0]

    plt.imshow(v.image_HSV)
    plt.show()

def edges_lined():# for an explanation of the Hough transform check https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
	rho = 1
	theta = np.pi/180
	threshold = 60
	min_line_length = 100
	max_line_gap = 25

	lines = cv2.HoughLinesP(v.image_edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)# creates the lines according to the Hough transform

	lined_image = np.copy(v.image) #change here to view other image variants with lines

	for line in lines:
		for x1, y1, x2, y2 in line:
			cv2.line(lined_image, (x1,y1),(x2,y2), (255,0,0), 3, cv2.LINE_AA)

	plt.imshow(lined_image)
	plt.show()

def image_enhance(): # trying to enhance the coloration of the images via CLAHE (Contrast Limited Adaptive Histogram Equalization)

    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8)) # determine CLAHE paramters (values based on recommendations)

    image_lab = cv2.cvtColor(v.image_copy, cv2.COLOR_RGB2LAB)  # convert from RGB to LAB, change v.image_copy here to view other images
    
    l, a, b = cv2.split(image_lab)  # split on 3 different channels

    l2 = clahe.apply(l)  # apply CLAHE to the L-channel

    image_lab = cv2.merge((l2,a,b))  # merge channels with the altered 'l' version
    image_enhanced = cv2.cvtColor(image_lab, cv2.COLOR_LAB2RGB)  # convert from LAB back to RGB

    plt.imshow(image_enhanced) # show
    plt.show()

'''
Call Functions:
Maybe create seperate function or file to run the functions below
'''

show_image()
#show_image_gray()
#hsv_filter()
#cut_out()
edges_lined()
#image_enhance()


