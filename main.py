from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import v

def default_image(): #shows the default/original image
    plt.imshow(v.image_copy)
    plt.show()

# Splitting channels in
def hsv_color_space(): # HSV color space

    #h = v.image_copy_HSV[:,:,0] #represents the 'Hue Image Analysis' which didnt quite get us the desired results
    s = v.image_copy_HSV[:,:,1] #represents the 'Saturation Image Analysis' which did get close to the desired results
    #v = v.image_copy_HSV[:,:,2] #represents the 'Value Image Analysis' which didnt quite get us the desired results

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

    mask_HSV = cv2.inRange(v.image_copy_HSV, lower_Hue, high_Hue)

    v.image_copy_HSV = np.copy(v.image_copy)

    v.image_copy_HSV[mask_HSV == 0] = [0,0,0]

    plt.imshow(v.image_copy_HSV)
    plt.show()

# Call Functions
# maybe create seperate function or file to run the functions below

default_image()
hsv_color_space()
cut_out()

#Test Branch:
#Currently working on 'Edge Detection' and 'Region of Interest'(abb.: RoI)

