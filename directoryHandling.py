# ==========================================================================================================================================================#
#                              directoryHandling.py - file for creating directories based on current time and moving previous rois into
# ==========================================================================================================================================================#

# =============================================================================
#   Imports
# =============================================================================

import os
import shutil
import glob
import errno
import matplotlib.pyplot as plt

import utils as xct

from PIL import Image
from datetime import datetime

from utils import VariableConfig as vxct
from extras import test_functions

# =============================================================================
#   Creating Variables
# =============================================================================
ROOT_DIR = os.path.abspath("../") # get parent directory
folderame = datetime.now().strftime("%Y(Y)__%m(M)__%d(D)__%H.%M(H).%S(s)")
newpath = ROOT_DIR+"/ColiChecker/images/image_3_storage/"+folderame

# =============================================================================
#   Moving Variables
# =============================================================================
source_dir = xct.path_folder_roi
target_dir = newpath
    
# =============================================================================
#   Functions
# =============================================================================
def createDir():
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def fillDir():

    file_names = os.listdir(source_dir)
        
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

#createDir()
#fillDir()