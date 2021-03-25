'''
Imports:
'''
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import variables as var

'''
Additional imports:
'''

from matplotlib.colors import hsv_to_rgb

'''
Variables:
'''
#light_color = light_orange = (1, 190, 200) # for images_testing
#dark_color = dark_orange = (18, 255, 255) # for images_testing

#light_color = light_white = (0, 0, 200) # for images_testing
#dark_color = dark_white = (145, 60, 255) # for images_testing

light_color = var.purple_light
dark_color = var.purple_dark


'''
Functions:
'''

def show_threshold(): # remove white space via HSV (variables: image_HSV, all )

    lb_square = np.full((10, 10, 3), light_color, dtype=np.uint8) / 255.0
    db_square = np.full((10, 10, 3), dark_color, dtype=np.uint8) / 255.0

    plt.subplot(1, 2, 1)
    plt.imshow(hsv_to_rgb(lb_square))
    plt.subplot(1, 2, 2)
    plt.imshow(hsv_to_rgb(db_square))
    plt.show()

def mask_black(): # altered copy from test_functions.py

    mask = cv2.inRange(var.image_HSV, light_color, dark_color)

    result = cv2.bitwise_and(var.image_copy, var.image_copy, mask=mask)

    plt.subplot(1, 2, 1)
    plt.imshow(mask, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.imshow(result)
    plt.show()

'''
Call Functions:
'''
show_threshold()
mask_black()