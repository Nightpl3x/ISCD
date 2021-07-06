# ==========================================================================================================================================================#
#                                               Mask R-CNN - Inspect Balloon Trained Model 
#                          Code and visualizations to test, debug, and evaluate the Mask R-CNN model on the balloon Dataset
# ==========================================================================================================================================================#

def MRCNN_Balloon(IMAGE_DIRECTORY_CAM, images_cam):
    # =============================================================================
    # Imports
    # =============================================================================
    import re
    import os
    import sys
    import math
    import time
    import random
    import skimage.io
    import numpy as np
    import tensorflow as tf
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    import directoryHandling as dH


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
    from mrcnn.config import Config
    from mrcnn import visualize
    from mrcnn.visualize import display_images
    import mrcnn.model as modellib
    from mrcnn.model import log

    # Import base Balloon config
    sys.path.append(os.path.join(ROOT_DIR, "Mask_RCNN/samples/balloon/"))  # find local version
    from Mask_RCNN.samples.balloon import balloon

    # Directory to save logs and trained model
    MODEL_DIR = os.path.join(ROOT_DIR, "logs")

    # Local path to balloon trained weights file
    BALLOON_MODEL_PATH = os.path.join('', ROOT_DIR+"/ISCD/Mask_RCNN/samples/balloon/mask_rcnn_balloon.h5")

    # Download Balloon trained weights from Releases if needed
    # Link for trained weights
    #    https://github.com/matterport/Mask_RCNN/releases

    # =======================================================================================================================================================================================================
    #                                                             Configurations
    #
    # We'll be using a model trained on the Balloon dataset. The configurations of this model are in the ```balloonConfig``` class in ```balloon.py```.
    # For inferencing, the configurations were modified a bit to fit the task. To do so, I sub-classed the ```balloonConfig``` class and overrode the attributes I needed to change.
    # =======================================================================================================================================================================================================
    config = balloon.BalloonConfig()
    BALLOON_DIR = os.path.join(ROOT_DIR, ROOT_DIR+"/ISCD/Mask_RCNN/samples/balloon") # path inside Mask_RCNN directory

    # Override the inference configurations
    class InferenceConfig(Config):

        # Override and sub-classes the config.py class

        # Name of the configurations
        NAME = "Balloon_Dataset"

        # Set batch size to 1 since we'll be running inference on one image at a time. 
        # Batch size = GPU_COUNT * IMAGES_PER_GPU

        # NUMBER OF GPUs to use. When using only a CPU, this needs to be set to 1.
        GPU_COUNT = 1
        # Run detection on one image at a time
        IMAGES_PER_GPU = 1

        # Number of steps per epoch
        STEPS_PER_EPOCH = 1000

        # Number of validation steps to run at the end of every epoch.
        # A bigger number improves accuracy of validation stats, but slows down
        VALIDATION_STEPS = 50

        # Backbone network architecture
        BACKBONE = "resnet101"

        # Number of classification classes (including background)
        NUM_CLASSES = 2  # For Balloon Dataset this equals Background + Balloon

        POST_NMS_ROIS_INFERENCE = 1000

        # If enabled, resizes instance masks to a smaller size to reduce memory load. Recommended when using high-resolution images.
        USE_MINI_MASK = True
        MINI_MASK_SHAPE = (56, 56)  # (height, width) of the mini-mask

        # Input image resizing
        IMAGE_RESIZE_MODE = "square"
        IMAGE_MIN_DIM = 800
        IMAGE_MAX_DIM = 1024

        # Number of color channels per image. RGB = 3, grayscale = 1, RGB-D = 4
        IMAGE_CHANNEL_COUNT = 3

        # Maximum number of ground truth instances to use in one image
        MAX_GT_INSTANCES = 100

        # Max number of final detections
        DETECTION_MAX_INSTANCES = 100

        # Minimum probability value to accept a detected instance
        # ROIs below this threshold are skipped
        DETECTION_MIN_CONFIDENCE = 0.7

        # Non-maximum suppression threshold for detection
        DETECTION_NMS_THRESHOLD = 0.3
        
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
        fig, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
        plt.close(fig)
        return ax

    # Load validation dataset
    dataset = balloon.BalloonDataset()
    dataset.load_balloon(BALLOON_DIR, 'val') # does not exist for balloon dataset

    # Must call before using the dataset
    dataset.prepare()

    # =============================================================================
    #                     Create Model and Load Trained Weights
    # =============================================================================
    # Create model object in inference mode.
    with tf.device(DEVICE):
        model = modellib.MaskRCNN(mode="inference", model_dir='mask_rcnn_balloon.hy', config=config) 

    weights_path = ROOT_DIR+"/ISCD/Mask_RCNN/samples/balloon/mask_rcnn_balloon.h5"

    # Load weights trained on Balloon
    model.load_weights(weights_path, by_name=True)

    # Class names
    # Balloon dataset consists of 1 class + Background

    # =============================================================================
    #                           Run Object Detection
    # =============================================================================
    results = model.detect([images_cam], verbose=1)
    r = results[0]

    # Display/Visualize results
    ax = get_ax(1)
    visualize.display_instances(images_cam,
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
        temp = skimage.io.imread(IMAGE_DIRECTORY_CAM)
        for j in range(temp.shape[2]):
            temp[:,:,j] = temp[:,:,j] * mask[:,:,i]
        plt.figure(figsize=(8,8))
        plt.imshow(temp)

        image_type = ".jpeg"
        dH.saveIMG(i, "Balloon", image_type)

        #plt.show()


if __name__ == '__main__':
    print ("\n  >Running MRCNN_Balloon.py by itself won't work on this version...\n")
else:
    print ("\n  >Importing MRCNN_Balloon.py...\n")
    image_type = ".jpeg"
    
