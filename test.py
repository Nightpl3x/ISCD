import os 
import glob
import skimage.io as io

ROOT_DIR = os.path.abspath("../") # get parent directory

def DirCAM_IMG():

    IMAGE_DIRECTORY_CAM = glob.glob(ROOT_DIR+"/ColiChecker/images/image_1_camera/*.jpeg") # create list based on image names --> strings
    IMAGE_DIRECTORY_CAM.sort() # sort list
    for image_cam_dir in IMAGE_DIRECTORY_CAM: 
        image_cam = io.imread(image_cam_dir)
        yield image_cam

def DirCAM_PATH():

    IMAGE_DIRECTORY_CAM = glob.glob(ROOT_DIR+"/ColiChecker/images/image_1_camera/*.jpeg") # create list based on image names --> strings
    IMAGE_DIRECTORY_CAM.sort() # sort list
    for image_cam_dir in IMAGE_DIRECTORY_CAM: 
        yield image_cam_dir
        
#image_cam = DirCAM()
#DirCAM()   

'''
path_folder_cam = os.listdir(ROOT_DIR+"/ColiChecker/images/image_1_camera")[0]
image_cam_dir = ROOT_DIR+"/ColiChecker/images/image_1_camera/"+path_folder_cam
image_cam = io.imread(ROOT_DIR+"/ColiChecker/images/image_1_camera/"+path_folder_cam)
'''

#print(ROOT_DIR) # parent directory
#print(path_folder_cam) # image name
#print(image_cam_dir) # image path
#print(image_cam) # image array