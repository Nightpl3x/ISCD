import os 
import skimage.io as io

ROOT_DIR = os.path.abspath("../") # get parent directory
path_folder_cam = os.listdir(ROOT_DIR+"/ColiChecker/images/image_1_camera")[0]
image_cam_dir = ROOT_DIR+"/ColiChecker/images/image_1_camera/"+path_folder_cam
image_cam = io.imread(ROOT_DIR+"/ColiChecker/images/image_1_camera/"+path_folder_cam)

print(ROOT_DIR) 
print(path_folder_cam) # parent directory
print(image_cam_dir) # image name
print(image_cam) # image array