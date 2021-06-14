# ==========================================================================================================================================================#
#                                                           directoryHandling.py 
#   file for creating directories based on current time and moving images from the image_2_rois directory into the image_3_storage directory
# ==========================================================================================================================================================#

# =============================================================================
#   Imports
# =============================================================================
import os
import shutil

import utils as xct

from datetime import datetime

# =============================================================================
#   Creating Variables
# =============================================================================
ROOT_DIR = os.path.abspath("../") # get parent directory

folderame = datetime.now().strftime("%Y(Y)__%m(M)__%d(D)__%H.%M(H).%S(s)")

newpath = ROOT_DIR+"/ColiChecker/images/image_3_storage/"+folderame

target_dir = newpath
    
# =============================================================================
#   Functions
# =============================================================================
def createDir():
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def fillDirRoi():

    source_dir_roi = xct.path_folder_roi
    file_names_roi = os.listdir(source_dir_roi)
    
    for file_name in file_names_roi:
        shutil.move(os.path.join(source_dir_roi, file_name), target_dir)

def fillDirCam(IMAGE_DIRECTORY_CAM):    

    source_dir_cam = IMAGE_DIRECTORY_CAM[:21]
    file_name_cam = IMAGE_DIRECTORY_CAM[22:]

    shutil.move(os.path.join(source_dir_cam, file_name_cam), target_dir)

if __name__ == '__main__':
    print ("\nRunning directoryHandling.py ...")
else:
    print ("\nImporting directoryHandling.py ...")

    #"images/image_1_camera\\18H_1000Z.jpeg"
    
