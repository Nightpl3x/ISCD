''' 
Imports:
'''
import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt

'''
Importing own module:
'''
import variables as v

''' 
Setup: (accordingly to the MS Coco Demo with some slight tweaks to match my purpose)
'''
# Root directory of the project
ROOT_DIR = os.path.abspath("../")

import warnings
warnings.filterwarnings("ignore")

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "Mask_RCNN/samples/coco/"))  # To find local coco configs version
from coco import coco # before: import coco


# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join('', "Mask_RCNN\samples\mask_rcnn_coco.h5") # relative trained weights path
# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)


'''
Configurations:
'''
class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

''' 
Function to get better control over folder and image paths
'''
def detectNmask(folder_path, abs_image_path):
    '''
    Create Model and load Training Weights:
    '''
    # Create model object in inference mode.
    model = modellib.MaskRCNN(mode="inference", model_dir='mask_rcnn_coco.hy', config=config) 

    # Load weights trained on MS-COCO
    model.load_weights('Mask_RCNN\samples\mask_rcnn_coco.h5', by_name=True) # an additonal model is also ready to use (needs relative path)


    '''
    Class names:
    '''
    # COCO Class names
    # Index of the class in the list is its ID. For example, to get ID of
    # the teddy bear class, use: class_names.index('teddy bear')

    class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
                'bus', 'train', 'truck', 'boat', 'traffic light',
                'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
                'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
                'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
                'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
                'kite', 'baseball bat', 'baseball glove', 'skateboard',
                'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
                'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
                'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
                'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
                'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
                'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
                'teddy bear', 'hair drier', 'toothbrush']

    '''
    Run Object Detection:
    '''
    # Load a random image from the images folder
    # Directory of images to run detection on

    IMAGE_DIR = os.path.join(ROOT_DIR, folder_path) # relative folder path
    #file_names = next(os.walk(IMAGE_DIR))[2]
    #image = skimage.io.imread(os.path.join(IMAGE_DIR, random.choice(file_names)))

    image = skimage.io.imread(abs_image_path) # only use absolute path
    # Run detection
    results = model.detect([image], verbose=1)

    # Visualize results
    r = results[0]
    visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                                class_names, r['scores'])


    ''' 
    Get and apply mask:
    '''
    mask = r['masks']
    mask = mask.astype(int)
    mask.shape

    for i in range(mask.shape[2]):
        temp = skimage.io.imread(abs_image_path)  # only use absolute path
        for j in range(temp.shape[2]):
            temp[:,:,j] = temp[:,:,j] * mask[:,:,i]
        plt.figure(figsize=(8,8))
        plt.imshow(temp)
        plt.show()

detectNmask(v.path_folder, v.path_image_abs)