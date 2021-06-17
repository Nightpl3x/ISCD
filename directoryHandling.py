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

# =============================================================================
# Main
# =============================================================================
def createDir():
    if not os.path.exists(xct.DirTxt.newpath):
        os.makedirs(xct.DirTxt.newpath)

def fillDirRoi():

    source_dir_roi = xct.path_folder_roi
    file_names_roi = os.listdir(source_dir_roi)
    
    for file_name in file_names_roi:
        shutil.move(os.path.join(source_dir_roi, file_name), xct.DirTxt.target_dir)

def fillDirCam(IMAGE_DIRECTORY_CAM):    

    source_dir_cam = IMAGE_DIRECTORY_CAM[:21]
    file_name_cam = IMAGE_DIRECTORY_CAM[22:]

    shutil.move(os.path.join(source_dir_cam, file_name_cam), xct.DirTxt.target_dir)

def createText(text_header):

    DirTxt = xct.DirTxt
    # create text file
    f = open(DirTxt.text_file_location, "w")
    f.write(text_header)
    f.close

def appendText(text):
    DirTxt = xct.DirTxt
    # append text to txt file
    f = open(DirTxt.text_file_location, "a")
    f.write(text)
    f.close()

if __name__ == '__main__':
    print ("\nRunning directoryHandling.py ...")
else:
    print ("\nImporting directoryHandling.py ...")

    