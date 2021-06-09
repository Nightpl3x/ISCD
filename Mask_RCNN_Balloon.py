# ==========================================================================================================================================================#
#                                               Mask R-CNN - Inspect Balloon Trained Model 
#                          Code and visualizations to test, debug, and evaluate the Mask R-CNN model on the Balloon Dataset
# ==========================================================================================================================================================#

# =============================================================================
# Imports
# =============================================================================
import os
import sys
import random
import math
import re
import time
import skimage.io
import numpy as np
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Custom import
import utils as xct

# Root directory of the project
ROOT_DIR = os.path.abspath("../../")

# Block unnecessary warnings
import warnings
warnings.filterwarnings("ignore")

# =============================================================================
# Import Mask_RCNN.mrcnn files, Balloon folder and Balloon Dataset
# =============================================================================

sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log

# Import base Balloon config
sys.path.append(os.path.join(ROOT_DIR, "Mask_RCNN/samples/balloon/"))  # To find local version
from Mask_RCNN.samples.balloon import balloon

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to Balloon trained weights file
BALLON_WEIGHTS_PATH = os.path.join('', ROOT_DIR+"/ColiChecker/Mask_RCNN/samples/balloon/mask_rcnn_balloon.h5") 

# Download Balloon trained weights from Releases if needed
# Link for trained weights
#    https://github.com/matterport/Mask_RCNN/releases

# ==========================================================================================================================================================
#                                                             Configurations
#
# We'll be using a model trained on the Balloon dataset. The configurations of this model are in the ```BalloonConfig``` class in ```balloon.py```.
# For inferencing, the configurations were modified a bit to fit the task. To do so, I sub-classed the ```BalloonConfig``` class and overrode the attributes I needed to change.
# ==========================================================================================================================================================
config = balloon.BalloonConfig()
BALLOON_DIR = os.path.join(ROOT_DIR, ROOT_DIR+"/ColiChecker/Mask_RCNN/samples/balloon") # path inside Mask_RCNN folder

# Override the training configurations with a few changes for inferencing.
class InferenceConfig(config.__class__):

    # Set batch size to 1 since we'll be running inference on one image at a time. 
    # Batch size = GPU_COUNT * IMAGES_PER_GPU
    # Run detection on one image at a time

    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    STEPS_PER_EPOCH = 1000
    DETECTION_MIN_CONFIDENCE = 0.7

config = InferenceConfig()
config.display()

# =========================================================================
# Device to load the neural network on.
# Useful if you're training a model on the same machine, in which case use CPU and leave the GPU for training.
# =========================================================================
DEVICE = "/cpu:0"  # /cpu:0 or /gpu:0

# Inspect the model in training or inference modes
# values: 'inference' or 'training'
# TODO: code for 'training' test mode not ready yet

TEST_MODE = "inference"

def get_ax(rows=1, cols=1, size=16):
    """Return a Matplotlib Axes array to be used in
    all visualizations in the notebook. Provide a
    central point to control graph sizes.
    
    Adjust the size attribute to control how big to render images
    """
    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    return ax

# Load validation dataset
dataset = balloon.BalloonDataset()
dataset.load_balloon(BALLOON_DIR, "val")

# Must call before using the dataset
dataset.prepare()

# =============================================================================
#                     Create Model and Load Trained Weights
# =============================================================================

# Create model object in inference mode
with tf.device(DEVICE):
    model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

weights_path = ROOT_DIR+"/ColiChecker/Mask_RCNN/samples/balloon/mask_rcnn_balloon.h5"

# Load weights trained on Balloon
model.load_weights(weights_path, by_name=True)

# Class names
# Balloon dataset consists only of 2 classes --> Background + Balloon

# =============================================================================
#                           Run Single Object Detection
# =============================================================================

# Directory of images to run detection on
#IMAGE_DIR = os.path.join(ROOT_DIR, xct.path_folder_abs)

# Load a random image from the images folder
#file_names = next(os.walk(IMAGE_DIR))[2]
#image = skimage.io.imread(os.path.join(IMAGE_DIR, random.choice(file_names)))

# Read image file
image = skimage.io.imread(xct.path_image_abs)

# Run object detection
results = model.detect([image], verbose=1)

# Display/Visualize results
ax = get_ax(1)
r = results[0]
visualize.display_instances(image, 
                            r['rois'], 
                            r['masks'], 
                            r['class_ids'], 
                            dataset.class_names, 
                            r['scores'], 
                            ax=ax,
                            title="Predictions")

# =============================================================================
#   Load mask and output images
# =============================================================================

mask = r['masks']
mask = mask.astype(int)
mask.shape

for i in range(mask.shape[2]):
    temp = skimage.io.imread(xct.path_image_abs)  # only use absolute path
    for j in range(temp.shape[2]):
        temp[:,:,j] = temp[:,:,j] * mask[:,:,i]
    plt.figure(figsize=(8,8))
    plt.imshow(temp)

#   ---------------target folder-----"/"----image name for target folder--------index-------file format
    image_name = xct.path_folder_roi+"/"+xct.path_image_abs[xct.last_slash:-5]+"{}".format(i)+"B.jpeg" # image name for saving, defintely needs other name template
    plt.savefig(image_name, bbox_inches='tight') # save images to new folder
    #plt.show()

'''
# output via splash function
splash = balloon.color_splash(image, r['masks'])
display_images([splash], cols=1)
'''

# =================================
#   Run colors_getHEX.py function
# =================================
import colors_getHEX as cgH
cgH.show_selected_images(cgH.images, cgH.COLORS['Cyan'], 55, 15) # analyzes whole images_rasp folder