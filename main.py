# Branch: Main
# Currently working on 'Edge Detection' and 'Region of Interest'(abb.: RoI)

import cv2
import numpy as np
import matplotlib.pyplot as plt
import variables as v

'''
Functions:
'''
img = v.image_copy # only for functions show_image() and show_image_gray()

def show_image(): # show desired image (variables: all )
    plt.imshow(img)
    plt.show()

def show_image_gray(): # show desired image in gray (mostly for edge detection) (variables: image_gray, image_edges)

	plt.imshow(img, cmap='gray')
	plt.show()

def image_enhance(): # enhance coloration via CLAHE (variables: all )

    # https://stackoverflow.com/questions/25008458/how-to-apply-clahe-on-rgb-color-images

    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8)) # determine CLAHE paramters (values based on recommendations)

    image_lab = cv2.cvtColor(v.image_copy, cv2.COLOR_RGB2LAB)  # convert from RGB to LAB, change v.image_copy here to view other images
    
    l, a, b = cv2.split(image_lab)  # split on 3 different channels

    l2 = clahe.apply(l)  # apply CLAHE to the L-channel

    image_lab = cv2.merge((l2,a,b))  # merge channels with the altered 'l' version
    image_enhanced = cv2.cvtColor(image_lab, cv2.COLOR_LAB2RGB)  # convert from LAB back to RGB

    plt.imshow(image_enhanced) # show
    plt.show()

def hsv_filter(): # split HSV color channels (variables: image_HSV )

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

def black_out(): # remove white space via HSV (variables: image_HSV, all )

    lower_Hue = np.array([160,0,0])
    high_Hue = np.array([180,255,255])

    mask_HSV = cv2.inRange(v.image_HSV, lower_Hue, high_Hue)

    v.image_HSV = np.copy(v.image_copy) # change here for other images

    v.image_HSV[mask_HSV == 0] = [0,0,0]

    plt.imshow(v.image_HSV)
    plt.show()

def edge_detection(): # detect lines via Hough transform (variables: image_edges, all )

    # https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html

	rho = 1
	theta = np.pi/180
	threshold = 60
	min_line_length = 100
	max_line_gap = 25

	lines = cv2.HoughLinesP(v.image_edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)# creates the lines according to the Hough transform

	lined_image = np.copy(v.image) # change here to view other image variants with lines

	for line in lines:
		for x1, y1, x2, y2 in line:
			cv2.line(lined_image, (x1,y1),(x2,y2), (255,0,0), 1, cv2.LINE_AA)

	plt.imshow(lined_image)
	plt.show()

def circle_detection(): #  detect circles via Hough transform (variables: image_edges, all )

    # https://learnopencv.com/hough-transform-with-opencv-c-python/amp/

    image_circles = cv2.HoughCircles(v.image_edges, cv2.HOUGH_GRADIENT, 1, 20, param1=20, param2=10, minRadius=25, maxRadius=35) # Apply Hough transform on the image

    if image_circles is not None: # Draw detected circles
        image_circles = np.uint16(np.around(image_circles))
        for i in image_circles[0, :]:
            
            cv2.circle(v.image_copy, (i[0], i[1]), i[2], (0, 0, 255), 1) # Draw outer circle
        
            cv2.circle(v.image_copy, (i[0], i[1]), 2, (255, 0, 0), 1) # Draw inner circle

    plt.imshow(v.image_copy)
    plt.show()


'''
Call Functions:
Maybe create seperate function or file to run the functions below
'''
#show_image()
#show_image_gray()
#image_enhance()
#hsv_filter()
#black_out()
#edge_detection()
#circle_detection()



