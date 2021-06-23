# ==========================================================================================================================================================#
#                                                           directoryHandling.py 
#   file for creating directories based on current time and moving images from the image_2_rois directory into the image_3_storage directory
# ==========================================================================================================================================================#

# =============================================================================
# Imports
# =============================================================================
import os
import glob
import shutil
import skimage.io as io
import matplotlib.pyplot as plt

from datetime import datetime

ROOT_DIR = os.path.abspath("../") # get parent directory

# =============================================================================
# Create Timestamp Directory
# =============================================================================
def setupDir():

    folderame = datetime.now().strftime("%Y(Y)__%m(M)__%d(D)__%H.%M(H).%S(s)")
    target_dir = ROOT_DIR+"/ColiChecker/images/image_3_storage/"+folderame
    text_file_location = target_dir+"/Results.txt"
    
    return folderame, target_dir, text_file_location

folderame, target_dir, text_file_location = setupDir()

def createDir():
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

# =============================================================================
# CAM Directory
# =============================================================================
def DirCAM():

    path_dir_cam = ROOT_DIR+"/ColiChecker/images/image_1_camera"
    image_cam_name = os.listdir(path_dir_cam)[0]
    IMAGE_DIRECTORY_CAM = path_dir_cam+"/"+image_cam_name 
    image_cam = io.imread(path_dir_cam+"/"+image_cam_name)

    return image_cam_name, IMAGE_DIRECTORY_CAM, image_cam

def fillDirCam(IMAGE_DIRECTORY_CAM):    

    shutil.move(os.path.join(IMAGE_DIRECTORY_CAM), target_dir)

def saveIMG(index, dataset_name, image_type):

    global path_dir_roi
    path_dir_roi = "images/image_2_rois" # relative path to ROI result images folder
    image_cam_name, _, _ = DirCAM()
    save_location = path_dir_roi+"/"
    image_appendix = "_by_"+dataset_name+"_{}".format(index)
    
    plt.savefig(save_location+image_cam_name+image_appendix+image_type, bbox_inches='tight') # save images to new directory

    return image_type

# =============================================================================
# ROI Directory
# =============================================================================
def DirROI(image_type):
    
    IMAGE_DIRECTORY_ROI = glob.glob(path_dir_roi+"/*"+image_type) # create list based on image names --> strings
    IMAGE_DIRECTORY_ROI.sort() # sort list
    images_roi = [io.imread(img) for img in IMAGE_DIRECTORY_ROI] # create additional list for storing images --> ndarrays

    return IMAGE_DIRECTORY_ROI, images_roi

def fillDirRoi():

    source_dir_roi = path_dir_roi
    file_names_roi = os.listdir(source_dir_roi)
    
    for file_name in file_names_roi:
        shutil.move(os.path.join(source_dir_roi, file_name), target_dir)


# =============================================================================
# Text file handling
# =============================================================================
def createText(text_header):
    # create text file
    f = open(text_file_location, "w")
    f.write(text_header)
    f.close

def appendText(text):
    # append text to txt file
    f = open(text_file_location, "a")
    f.write(text)
    f.close()


if __name__ == '__main__':
    print ("\nRunning directoryHandling.py ...")
else:
    print ("\nImporting directoryHandling.py ...")

    
