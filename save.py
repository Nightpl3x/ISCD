# ==========================================================================================================================================================#
#                                                   save.py - Beta file for image file handling
# ==========================================================================================================================================================#

# =============================================================================
# Imports
# =============================================================================
import glob
import matplotlib.pyplot as plt
import utils as xct

from PIL import Image

# ==============================================================
# checks all images in abs folder for .jpeg and and sorts them 
# (maybe use time stamps for future sorting)
# ==============================================================
e = xct.path_folder_abs+"/*.jpeg" 
filenames = glob.glob(e)
filenames.sort()

for img in filenames:

# ========================
# Print Image Name
# ========================
    img = Image.open(img)
    print(img.filename)

# ========================
# Output image
# ========================
    plt.imshow(img)
    plt.show()
    print(img)

# ========================
# *empty*
# ========================


    
