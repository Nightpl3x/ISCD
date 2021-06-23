import os 
import cv2
import glob
import skimage.io as io

ROOT_DIR = os.path.abspath("../") # get parent directory

path_folder_cam = os.listdir(ROOT_DIR+"/ColiChecker/images/image_1_camera")[0]
image_cam_dir = ROOT_DIR+"/ColiChecker/images/image_1_camera/"+path_folder_cam
image_cam = io.imread(ROOT_DIR+"/ColiChecker/images/image_1_camera/"+path_folder_cam)


print(ROOT_DIR) # parent directory
print(path_folder_cam) # image name
print(image_cam_dir) # image path
#print(image_cam) # image array

def DirCAM(image_type):
    
    IMAGE_DIRECTORY_CAM = glob.glob("images/image_1_camera"+image_type) # create list based on image names --> strings
    IMAGE_DIRECTORY_CAM.sort() # sort list
    images_cam = [cv2.imread(img) for img in IMAGE_DIRECTORY_CAM] # create additional list for storing images --> ndarrays
    images_cam = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in images_cam] # convert from bgr back to rgb

    return IMAGE_DIRECTORY_CAM, images_cam

IMAGE_DIRECTORY_CAM, images_cam = DirCAM("./*.jpeg")

print(IMAGE_DIRECTORY_CAM)
#print(images_cam)