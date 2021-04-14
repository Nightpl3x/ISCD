# State: 
# ToDo: 
'''
Imports:
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import variables as v

'''
Additional Imports:
'''
from scipy import ndimage
from skimage.color import rgb2gray
from sklearn.cluster import KMeans

'''
Code:
'''
def region_segmentation(image):

    gray = rgb2gray(image)
    gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
    for i in range(gray_r.shape[0]):
        if gray_r[i] > gray_r.mean():
            gray_r[i] = 3
        elif gray_r[i] > 0.5:
            gray_r[i] = 2
        elif gray_r[i] > 0.25:
            gray_r[i] = 1
        else:
            gray_r[i] = 0

    gray = gray_r.reshape(gray.shape[0],gray.shape[1])
    plt.imshow(gray, cmap='gray')
    plt.show()

def edge_segmentation(image):

    gray = rgb2gray(image)

    out_l = ndimage.convolve(gray, v.kernel_laplacian, mode='reflect')
    plt.imshow(out_l, cmap='gray')
    plt.show()


def cluster_segmentation(path):

    pic = plt.imread(path)/255  # divide by 255 to set pixel values between 0 and 1
    pic_n = pic.reshape(pic.shape[0]*pic.shape[1], pic.shape[2])
    pic_n.shape

    kmeans = KMeans(n_clusters=5, random_state=0).fit(pic_n)
    pic2show = kmeans.cluster_centers_[kmeans.labels_]

    cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2])

    plt.imshow(cluster_pic)
    plt.show()

''' 
Call:
'''
#region_segmentation(v.image_ext)
#edge_segmentation(v.image_ext)
#cluster_segmentation('images_testing/1.jpeg')