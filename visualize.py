'''
Imports:
'''
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import variables as v

'''
Additional imports:
'''
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

def rgb_visualize():
    '''
    Setup:
    '''
    img = v.image_copy
    r, g, b = cv2.split(img)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")

    '''
    Create Graphic:
    '''
    pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    plt.show()



'''
Call Functions:
'''
#rgb_visualize()
