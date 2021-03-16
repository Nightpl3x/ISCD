from cv2 import cv2 #do not switch to the sole 'import cv2' the code may work but for me it does not
import matplotlib.pyplot as plt
import numpy as np

# image processing variables
# read images via the image path (Important: Only use the pah of your current device and comment the other out!)
image = cv2.imread('images\S1_Kovacs_100Z.jpeg') # :Workplace relative path
#image = cv2.imread('C:/Users/skyli/Documents/VisualStudio/Python/Python Projects/ColiChecker/images/S2_Kovacs_10000Z.jpeg') # :Homeplace absolute path
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #convert to rgb just to be safe later on
image_copy = np.copy(image) #copying the image so we dont alter the original
image_copy_HSV = cv2.cvtColor(image_copy, cv2.COLOR_RGB2HSV) #create a copy to test hsv

def default_image(image_copy): #shows the default/original image
    plt.imshow(image_copy)
    plt.show()

# Splitting channels in
def hsv_color_space(image_copy): # HSV color space

    #h = image_copy_HSV[:,:,0] #represents the 'Hue Image Analysis' which didnt quite get us the desired results
    s = image_copy_HSV[:,:,1] #represents the 'Saturation Image Analysis' which did get close to the desired results
    #v = image_copy_HSV[:,:,2] #represents the 'Value Image Analysis' which didnt quite get us the desired results

    fig, (( ax1 ), ( ax2 )) = plt.subplots(2,1, figsize=(20,10)) #2 displays rows, 1 displays columns; 
    # check https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py for more information

    # Titles
    ax1.set_title('Saturation')
    ax2.set_title('Saturation_gray')

    # Images
    ax1.imshow(s)
    ax2.imshow(s, cmap='gray')

    plt.show()

def cut_out(image_copy_HSV): # Cutting out/Black out image !!! needs improving, too much whitespace left

    lower_Hue = np.array([160,0,0])
    high_Hue = np.array([180,255,255])

    mask_HSV = cv2.inRange(image_copy_HSV, lower_Hue, high_Hue)

    image_copy_HSV = np.copy(image_copy)

    image_copy_HSV[mask_HSV == 0] = [0,0,0]

    plt.imshow(image_copy_HSV)
    plt.show()

# Call Functions
# maybe create seperate function or file to run the functions below
default_image(image_copy)
hsv_color_space(image_copy)
cut_out(image_copy_HSV)
