import cv2
from skimage import io
import numpy as np
'''
Virtual Environment:
'''
#   .\env\Scripts\activate
#   deactivate

'''
Image selection:
'''
path_folder_abs = 'D:/Christian_Ohlhäuser/Bildauswertung/ColiChecker/images/_original2' 
path_folder = path_folder_abs[50 :]

path_image_abs = 'D:/Christian_Ohlhäuser/Bildauswertung/ColiChecker/images/_original/44H_10000Z.jpeg'
path_image = path_image_abs[50 :]


'''
Fork Images:
'''
image = io.imread(path_image_abs)
#image = cv2.imread(path_image_abs, cv2.IMREAD_COLOR) # doesnt work amymore, maybe will have to change the ext and int image names

image_int = np.copy(image) # copying the image so we dont alter the original
image_cp1 = np.copy(image_int) # copying the image for comparision purposes

image_ext = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert to rgb for other modules as opencv uses bgr by default but doesnt show it to the user
image_cp2= np.copy(image_ext) # copying the image for comparision purposes

image_blank = np.zeros_like(image) # just a blank image

'''
Image processing variables:
'''
# Change Color Model
image_gray1 = cv2.cvtColor(image_int, cv2.COLOR_BGR2GRAY) # turn rgb image into a grayed version
image_gray2 = cv2.cvtColor(image_ext, cv2.COLOR_RGB2GRAY) # turn rgb image into a grayed version

image_HSV1 = cv2.cvtColor(image_int, cv2.COLOR_BGR2HSV) # create image in hsv model
image_HSV2 = cv2.cvtColor(image_ext, cv2.COLOR_RGB2HSV) # create image in hsv model

# Blurring methods
image_median1 = cv2.medianBlur(image_gray1, ksize = 7) # Blur image to reduce noise(7 indicates the level of blurring)
image_median2 = cv2.medianBlur(image_gray2, ksize = 7) # Blur image to reduce noise(7 indicates the level of blurring)

image_gaussian1 = cv2.GaussianBlur(image_gray1,(7,7),1) 
image_gaussian2 = cv2.GaussianBlur(image_gray2,(7,7),1)

# Edge Detection
image_canny1 = cv2.Canny(image_gaussian1, threshold1 = 40, threshold2 = 50) # uses Hough transform to make edges more visible
image_canny2 = cv2.Canny(image_gaussian2, threshold1 = 40, threshold2 = 50) # uses Hough transform to make edges more visible

'''
Kernels: https://en.wikipedia.org/wiki/Kernel_(image_processing)
'''
# Basic Kernels
kernel = np.ones((5,5), np.uint8) # 5x5 Einheitsmatrix mostly suffiecient
kernel2 = np.ones((7,7), np.uint8) # 7x7 Einheitsmatrix go with this most of the time

# Custom kernels
kernel3 = np.array(([0, 1, 0], [1, 1, 1], [0, 1, 0]),dtype='uint8') # Wikipedia Test Matrix

kernel_sharp = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) 

#kernel_sobel_horizontal = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]]) 
#kernel_sobel_vertical = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])

kernel_laplacian = np.array([[1, 1, 1],[1, -8, 1],[1, 1, 1]]) # basically a merge of the previous two


# Kernel test variables
image_kerneled1 = cv2.filter2D(image_int, -1, kernel2) # alter image via kernels
image_kerneled2 = cv2.filter2D(image_ext, -1, kernel2) # alter image via kernels

'''
Unused image processing variables:
'''
image_resized1 = cv2.resize(image_int, (600, 400)) # function to resize image
image_resized2 = cv2.resize(image_ext, (600, 400)) # function to resize image

'''
General Functions:
'''
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver