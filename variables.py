import cv2
import numpy as np
'''
Virtual Environment:
'''
#   .\env\Scripts\activate
#   deactivate

'''
Image selection:
'''
image = cv2.imread('images/S2_Kovacs_10000Z.jpeg', cv2.IMREAD_COLOR) # :Workplace relative path
image_int = np.copy(image) # copying the image so we dont alter the original
image_ext = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # convert to rgb for other modules as opencv uses bgr by default but doesnt show it to the user

'''
Image processing variables:
'''
image_gray = cv2.cvtColor(image_int, cv2.COLOR_RGB2GRAY) # turn rgb image into a grayed version 

image_HSV = cv2.cvtColor(image_int, cv2.COLOR_RGB2HSV) # create image in hsv for the color schemes extraction
                                    
#                                  low , high threshold 
image_edges = cv2.Canny(image_int, 100 , 150) # makes edges more visible, used for the Hough transform in edges_lined()

'''
Kernels: https://en.wikipedia.org/wiki/Kernel_(image_processing)
'''
kernel = np.ones((5,5), np.uint8) # 5x5 Einheitsmatrix
kernel2 = np.ones((7,7), np.uint8) # 7x7 Einheitsmatrix

kernel3 = np.array(([0, 1, 0],
					[1, 1, 1],
					[0, 1, 0]),dtype='uint8') # Wikipedia Test Matrix

kernel_sharp = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) 

image_kernel = cv2.filter2D(image_int, -1, kernel) # 'enhance' image via kernels (image variable is for testing only)

'''
Unused image processing variables:
'''
image_blur = cv2.medianBlur(image_int, 5) # Blur image to reduce noise(5 indicates the level of blurring)

image_resized = cv2.resize(image_int, (1200, 600)) # function to resize image, if ever needed

'''
General Functions:
'''
def rgbtobgr(image):
    image_int = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    return image_int

def bgrtorgb(image):
    image_int = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    return image_int

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