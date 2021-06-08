# ==========================================================================================================================================================#
#                                     test.py - Beta file for image file handling with the according image file names and other test
# ==========================================================================================================================================================#

# File is obsolete as I integrate its needed parts into the main files 
# =============================================================================
#   Imports
# =============================================================================
import glob
import matplotlib.pyplot as plt

from PIL import Image

import utils as xct
from utils import VariableConfig as vxct

from extras import test_functions

def show_image(img): # show desired image (variables: all )

    plt.imshow(img)
    plt.show()

#show_image(vxct.image_ext)
#test_functions.show_image(vxct.image_ext)

'''
# ==============================================================
# checks all images in abs folder for .jpeg and and sorts them 
# (maybe use time stamps for future sorting)
# ==============================================================
e = xct.path_folder_abs+"/*.jpeg" 
filenames = glob.glob(e)
filenames.sort()

for img in filenames:

# ========================
#   Print Image Name
# ========================
    img = Image.open(img)
    print(img.filename)

# ========================
#   Output image
# ========================
    plt.imshow(img)
    plt.show()
    print(img)

# ========================
#   *empty*
# ========================
'''