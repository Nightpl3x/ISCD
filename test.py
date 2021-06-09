# ==========================================================================================================================================================#
#                                                          directoryHandling.py 
#               file for moving images in the image_1_camera directory into the corresponding directory below the image_3_storage directory
# ==========================================================================================================================================================#

# =============================================================================
#   Imports
# =============================================================================

import os
import shutil
import glob
import errno
import cv2
import matplotlib.pyplot as plt

import utils as xct

from PIL import Image
from datetime import datetime

from utils import VariableConfig as vxct
from extras import test_functions

# ==========================================================================
#   Setup
# ==========================================================================

e = xct.path_folder_cam+"/*.jpeg" # check ROI result folder for images

IMAGE_DIRECTORY = glob.glob(e) # create list based on image names --> strings
IMAGE_DIRECTORY.sort()         # sort list
images = [cv2.imread(img) for img in IMAGE_DIRECTORY] # create additional list for storing images --> ndarrays
images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in images] # convert from bgr back to rgb
