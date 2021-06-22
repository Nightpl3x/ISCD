# ==========================================================================================================================================================#
#                                                           directoryHandling.py 
#   file for creating directories based on current time and moving images from the image_2_rois directory into the image_3_storage directory
# ==========================================================================================================================================================#

# =============================================================================
#   Imports
# =============================================================================
import os
import glob
import cv2
import shutil
import matplotlib.pyplot as plt

from PIL import Image
from datetime import datetime


import utils as xct

ROOT_DIR = os.path.abspath("../") # get parent directory

# =============================================================================
# Create Result Text file
# =============================================================================
class DirTxt(object):
    folderame = datetime.now().strftime("%Y(Y)__%m(M)__%d(D)__%H.%M(H).%S(s)")
    newpath = ROOT_DIR+"/ColiChecker/images/image_3_storage/"+folderame
    target_dir = newpath
    text_file_location = newpath+"/Results.txt"

# =============================================================================
# Timestamp Directory
# =============================================================================
def createDir():
    if not os.path.exists(DirTxt.newpath):
        os.makedirs(DirTxt.newpath)

# =============================================================================
# ROI Directory
# =============================================================================
path_folder_roi = "images/image_2_rois" # relative path to ROI result images folder

def DirROI():

    IMAGE_DIRECTORY_ROI = glob.glob(path_folder_roi+"/*.jpeg") # create list based on image names --> strings
    IMAGE_DIRECTORY_ROI.sort() # sort list
    images_roi = [cv2.imread(img) for img in IMAGE_DIRECTORY_ROI] # create additional list for storing images --> ndarrays
    images_roi = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in images_roi] # convert from bgr back to rgb

    return IMAGE_DIRECTORY_ROI, images_roi

def fillDirRoi():

    source_dir_roi = path_folder_roi
    file_names_roi = os.listdir(source_dir_roi)
    
    for file_name in file_names_roi:
        shutil.move(os.path.join(source_dir_roi, file_name), DirTxt.target_dir)

# =============================================================================
# CAM Directory
# =============================================================================
path_folder_cam = "images/image_1_camera" # relative path to camera images folder

def DirCAM():
    
    IMAGE_DIRECTORY_CAM = glob.glob(path_folder_cam+"/*.jpeg") # create list based on image names --> strings
    IMAGE_DIRECTORY_CAM.sort() # sort list
    images_cam = [cv2.imread(img) for img in IMAGE_DIRECTORY_CAM] # create additional list for storing images --> ndarrays
    images_cam = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in images_cam] # convert from bgr back to rgb

    return IMAGE_DIRECTORY_CAM, images_cam


def fillDirCam(IMAGE_DIRECTORY_CAM):    

    source_dir_cam = IMAGE_DIRECTORY_CAM[:21]
    file_name_cam = IMAGE_DIRECTORY_CAM[22:]

    shutil.move(os.path.join(source_dir_cam, file_name_cam), DirTxt.target_dir)

# =============================================================================
# Text file handling
# =============================================================================

def createText(text_header):
    # create text file
    f = open(DirTxt.text_file_location, "w")
    f.write(text_header)
    f.close

def appendText(text):
    # append text to txt file
    f = open(DirTxt.text_file_location, "a")
    f.write(text)
    f.close()



def saveIMG(IMAGE_DIRECTORY_CAM, index, name):
    
    with Image.open(IMAGE_DIRECTORY_CAM) as cam_image_title:
        cam_image_name = cam_image_title.filename

    last_cam_in_str = cam_image_name.rfind("camera") # find last occurring "camera" in string of image path
    last_dot_in_str = cam_image_name.rfind(".") # find last occurring "." in string of image path
    image_name = cam_image_name[last_cam_in_str+7:last_dot_in_str]

    save_location = path_folder_roi+"/"
    image_appendix = "_by_"+name+"_{}".format(index)
    image_type = ".jpeg"
    
    plt.savefig(save_location+image_name+image_appendix+image_type, bbox_inches='tight') # save images to new directory

if __name__ == '__main__':
    print ("\nRunning directoryHandling.py ...")
else:
    print ("\nImporting directoryHandling.py ...")

    
