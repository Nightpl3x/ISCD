# ==========================================================================================================================================================#
#                                               Mask R-CNN - Inspect Coco Trained Model 
#                          Code and visualizations to test, debug, and evaluate the Mask R-CNN model on the Coco Dataset
# ==========================================================================================================================================================#

def MRCNN_Coco(IMAGE_DIRECTORY_CAM,images_cam):
    # =============================================================================
    # Basic Imports + Setup for image_1_camera check
    # =============================================================================
    import cv2
    import glob
    import utils as xct
    import directoryHandling as dH

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
    # Import Mask_RCNN.mrcnn files, Coco directory and Coco Dataset
    # =============================================================================
    sys.path.append(ROOT_DIR)  # find local version of the library
    from mrcnn import utils
    from mrcnn import visualize
    from mrcnn.visualize import display_images
    import mrcnn.model as modellib
    from mrcnn.model import log

    # Import base COCO config
    sys.path.append(os.path.join(ROOT_DIR, "Mask_RCNN/samples/coco/"))  # find local version
    from Mask_RCNN.samples.coco import coco

    # Directory to save logs and trained model
    MODEL_DIR = os.path.join(ROOT_DIR, "logs")

    # Local path to Coco trained weights file
    COCO_MODEL_PATH = os.path.join('', ROOT_DIR+"/ColiChecker/Mask_RCNN/samples/coco/mask_rcnn_coco.h5")

    # Download COCO trained weights from Releases if needed
    if not os.path.exists(COCO_MODEL_PATH):
        utils.download_trained_weights(COCO_MODEL_PATH)

    # =======================================================================================================================================================================================================
    #                                                             Configurations
    #
    # We'll be using a model trained on the MS-COCO dataset. The configurations of this model are in the ```CocoConfig``` class in ```coco.py```.
    # For inferencing, the configurations were modified a bit to fit the task. To do so, I sub-classed the ```CocoConfig``` class and overrode the attributes I needed to change.
    # =======================================================================================================================================================================================================
    config = coco.CocoConfig()
    COCO_DIR = os.path.join(ROOT_DIR, ROOT_DIR+"/ColiChecker/Mask_RCNN/samples/coco") # path inside Mask_RCNN directory

    # Override the training configurations with a few changes for inferencing.
    class InferenceConfig(coco.CocoConfig):

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
    dataset = coco.CocoDataset()
    #dataset.load_coco(COCO_DIR, "val") # does not exist for coco dataset

    # Must call before using the dataset
    dataset.prepare()

    # =============================================================================
    #                     Create Model and Load Trained Weights
    # =============================================================================
    # Create model object in inference mode.
    with tf.device(DEVICE):
        model = modellib.MaskRCNN(mode="inference", model_dir='mask_rcnn_coco.hy', config=config) 

    weights_path = ROOT_DIR+"/ColiChecker/Mask_RCNN/samples/coco/mask_rcnn_coco.h5"

    # Load weights trained on MS-COCO
    model.load_weights(weights_path, by_name=True)

    # Class names
    class_names = ['Object' for _ in range(90)] # Coco dataset consists of 89 classes + Background

    # =============================================================================
    #                           Run Object Detection
    # =============================================================================
    results = model.detect([images_cam], verbose=1)

    # Display/Visualize results
    ax = get_ax(1)
    r = results[0]
    visualize.display_instances(images_cam,
                                r['rois'], 
                                r['masks'], 
                                r['class_ids'], 
                                class_names, 
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

        dH.saveIMG(IMAGE_DIRECTORY_CAM, i, "Coco")

        #plt.show()


if __name__ == '__main__':
    print ("\nRunning MRCNN_Coco.py by itself won't work on this version ...")
else:
    print ("\nImporting MRCNN_Coco.py ...")

    
