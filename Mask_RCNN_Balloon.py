# ==========================================================================================================================================================#
#                                               Mask R-CNN - Inspect Balloon Trained Model 
#                          Code and visualizations to test, debug, and evaluate the Mask R-CNN model on the Balloon Dataset
# ==========================================================================================================================================================#

# =============================================================================
# Basic Imports + Setup for image_1_camera check
# =============================================================================
import cv2
import glob
import utils as xct

# Directory of images to run detection on

e = xct.path_folder_cam+"/*.jpeg" # search camera directory for images

IMAGE_DIRECTORY = glob.glob(e) # create list based on image names --> strings
IMAGE_DIRECTORY.sort()         # sort list
images_cam = [cv2.imread(img) for img in IMAGE_DIRECTORY] # create additional list for storing images --> ndarrays
images_cam = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in images_cam] # convert from bgr back to rgb

# =============================================================================
# Check image_1_camera directory for images
# =============================================================================
if len(images_cam) == 0:
    print("\n Sorry but there are no pictures in here...")

elif len(images_cam) > 0:

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

    from PIL import Image

    # Root directory of the project
    ROOT_DIR = os.path.abspath("../")

    # Block unnecessary warnings
    import warnings
    warnings.filterwarnings("ignore")

    # =============================================================================
    # Import Mask_RCNN.mrcnn files, Balloon directory and Balloon Dataset
    # =============================================================================

    sys.path.append(ROOT_DIR)  # find local version of the library
    from mrcnn import utils
    from mrcnn import visualize
    from mrcnn.visualize import display_images
    import mrcnn.model as modellib
    from mrcnn.model import log

    # Import base Balloon config
    sys.path.append(os.path.join(ROOT_DIR, "Mask_RCNN/samples/balloon/"))  # find local version
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
    BALLOON_DIR = os.path.join(ROOT_DIR, ROOT_DIR+"/ColiChecker/Mask_RCNN/samples/balloon") # path inside Mask_RCNN directory

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
    #                           Run Object Detection
    # =============================================================================

    for index in range(len(images_cam)):

        # Run object detection
        results = model.detect([images_cam[index]], verbose=1)

        # Display/Visualize results
        ax = get_ax(1)
        r = results[0]
        visualize.display_instances(images_cam[index],
                                    r['rois'], 
                                    r['masks'], 
                                    r['class_ids'], 
                                    dataset.class_names, 
                                    r['scores'],
                                    ax=ax,
                                    title="Predictions")

        # =============================================================================
        # Load mask and output images
        # =============================================================================

        mask = r['masks']
        mask = mask.astype(int)
        mask.shape

        for i in range(mask.shape[2]):
            temp = images_cam[index]
            for j in range(temp.shape[2]):
                temp[:,:,j] = temp[:,:,j] * mask[:,:,i]
            plt.figure(figsize=(8,8))
            plt.imshow(temp)

            with Image.open(IMAGE_DIRECTORY[index]) as cam_image:
                cam_image_name = cam_image.filename

            last_cam = cam_image_name.rfind("camera") # find last occurring "camera" in string of image path

        #---------------target directory-----"/"----image name in target directory--------index-------file format
            image_name = xct.path_folder_roi+"/"+cam_image_name[last_cam+7:-5]+"_{}".format(i)+"B.jpeg" # image name for saving, could use other name template
            plt.savefig(image_name, bbox_inches='tight') # save images to new directory
            #plt.show()

    # =================================
    #  Run external functions
    # =================================
    
    print("\n")
    import colorExtraction as cE
    cE.show_selected_images(cE.images_roi, cE.COLORS['Cyan'], 55, 15) # analyzes whole image_2_rois directory

    import directoryHandling as dH
    dH.createDir() # create directory with timestamp to move images to
    dH.fillDirRoi() # move roi images into directory
    dH.fillDirCam() # move camera image into directory