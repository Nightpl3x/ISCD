'''
Imports:
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import utils as xct

'''
Functions:
'''
def show_image(img): # show desired image (variables: all )

    plt.imshow(img)
    plt.show()

def show_image_gray(img): # show desired image in gray (mostly for edge detection) (variables: image_gray, image_edges)

	plt.imshow(img, cmap='gray')
	plt.show()

def image_enhance(img): # enhance coloration via CLAHE (variables: all )

    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8)) # determine CLAHE paramters (values based on recommendations)

    image_lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)  # convert from RGB to LAB, change image_circled here to view other images
    
    l, a, b = cv2.split(image_lab)  # split on 3 different channels

    l2 = clahe.apply(l)  # apply CLAHE to the L-channel

    image_lab = cv2.merge((l2,a,b))  # merge channels with the altered 'l' version
    image_enhanced = cv2.cvtColor(image_lab, cv2.COLOR_LAB2RGB)  # convert from LAB back to RGB

    plt.imshow(image_enhanced) # show
    plt.show()

def hsv_filter(image_HSV): # split HSV color channels (variables: image_HSV )

    #h = image_HSV[:,:,0] #represents the 'Hue Image Analysis' which didnt quite get us the desired results
    s = image_HSV[:,:,1] #represents the 'Saturation Image Analysis' which did get close to the desired results
    #v = image_HSV[:,:,2] #represents the 'Value Image Analysis' which didnt quite get us the desired results

    fig, (( ax1 ), ( ax2 )) = plt.subplots(2,1, figsize=(20,10)) #2 displays rows, 1 displays columns; 
    # check info.py for further information

    # Titles
    ax1.set_title('Saturation')
    ax2.set_title('Saturation_gray')

    # Images
    ax1.imshow(s)
    ax2.imshow(s, cmap='gray')

    plt.show()

def mask_black(image_HSV): # remove white space via HSV (variables: image_HSV, all )

    lower_Hue = np.array([160,0,0]) # adjustable better method in color branch 
    high_Hue = np.array([180,255,255]) # adjustable, better method in color branch

    mask_HSV = cv2.inRange(image_HSV, lower_Hue, high_Hue)

    image_HSV = np.copy(xct.image) # adjustable to other images variants

    image_HSV[mask_HSV == 0] = [0,0,0]

    plt.imshow(image_HSV)
    plt.show()

def edge_detection(image_canny): # detect lines via Hough transform (variables: image_edges, all )

	rho = 1
	theta = np.pi/180
	threshold = 60
	min_line_length = 100
	max_line_gap = 25

	lines = cv2.HoughLinesP(image_canny, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)# creates the lines according to the Hough transform

	image_lined = np.copy(xct.image)

	for line in lines:
		for x1, y1, x2, y2 in line:
			cv2.line(image_lined, (x1,y1),(x2,y2), (255,0,0), 1, cv2.LINE_AA)

	plt.imshow(image_lined)
	plt.show()

def circle_detection(image_canny): # detect circles via Hough transform (variables: image_edges, all )

    image_circles = cv2.HoughCircles(image_canny, cv2.HOUGH_GRADIENT, 1, 20, param1=20, param2=10, minRadius=25, maxRadius=35) # Apply Hough transform on the image

    if image_circles is not None: # Draw detected circles
        image_circles = np.uint16(np.around(image_circles))
        for i in image_circles[0, :]:

            image_circled = np.copy(xct.image) # adjustable to other images varaints
            
            cv2.circle(image_circled, (i[0], i[1]), i[2], (0, 0, 255), 1) # Draw outer circle
        
            cv2.circle(image_circled, (i[0], i[1]), 2, (255, 0, 0), 1) # Draw inner circle

    plt.imshow(image_circled)
    plt.show()


'''
Call Functions:
'''
show_image(xct.image)
#show_image_gray()
#image_enhance(xct.image_ext)
#hsv_filter(xct.image_HSV2)
#mask_black(xct.image_HSV2)
#edge_detection(xct.image_canny2)
#circle_detection(xct.image_canny2)



