# ==========================================================================================================================================================#
#                                                   main.py - handles script execution
# ==========================================================================================================================================================#

# =============================================================================
# Imports
# =============================================================================
import os
import sys
import time
import random
import skimage.io as io

ROOT_DIR = os.path.abspath("../") # get parent directory

# =============================================================================
# run()
# =============================================================================

def cycle():

    try:

        print("\n=================================================")
        print("\nReading current state\n...")
        print("\n=================================================")
        with open("runtime.txt") as f:
            lines = f.readlines()

        # =================================
        # PHASE 0: 
        # Creating Directory
        # =================================
        if lines[0] == "Phase: 0\n":
            print("__________________________________")
            print("\nInitializing script...")
            print("__________________________________")
            # =============================================================================
            # Check image_1_camera directory for images
            # =============================================================================
            import directoryHandling as dH
            path_dir_cam, _, IMAGE_DIRECTORY_CAM, _ = dH.DirCAM() # read directory state and take first image if present

            file_names = next(os.walk(path_dir_cam))[2] #iterate through generator
            images_cam = io.imread(os.path.join(path_dir_cam, random.choice(file_names))) # get random Image by generator

            # =============================================================================
            # Create results file into timestamp directory
            # ============================================================================= 
            print("__________________________________")   
            print("\nCreating directory...")
            print("__________________________________")
            
            dH.setupDir() # directory with current time

            # =============================================================================
            # Overwrite runtime.txt with next Phase and Timestamp Directory name
            # =============================================================================      
            with open("runtime.txt") as f:
                lines = f.readlines()
                lines[0] = "Phase: 1\n"
            with open("runtime.txt", "w") as f:
                f.writelines(lines)   

        # =================================
        # PHASE 1:
        # Object Detection
        # =================================            
        elif lines[0] == "Phase: 1\n":
            print("__________________________________")
            print("\nInitializing Object Detection...")
            print("__________________________________")
            # =============================================================================
            # Get first image in image_1_camera directory for the object detection
            # =============================================================================
            from directoryHandling import DirCAM
            _, image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = DirCAM() # read directory state and take first image if present

            # =================================
            #  Run first Dataset
            # =================================
            import MRCNN_Balloon as mrb
            mrb.MRCNN_Balloon(IMAGE_DIRECTORY_CAM, images_cam)

            # =============================================================================
            # Overwrite runtime.txt with next Phase
            # =============================================================================  
            with open("runtime.txt") as f:
                lines = f.readlines()
                lines[0] = "Phase: 2\n"
            with open("runtime.txt", "w") as f:
                f.writelines(lines)   

        # =================================
        # PHASE 2:
        # Color Extraction
        # =================================            
        elif lines[0] == "Phase: 2\n":
            print("__________________________________")
            print("\nInitializing Color Analysis...")
            print("__________________________________")
            # =================================
            #  Analyze ROIs
            # =================================
            import colorExtraction as cE 
            from utils import COLORS
            from MRCNN_Balloon import image_type
            from directoryHandling import DirROI

            IMAGE_DIRECTORY_ROI, images_roi = DirROI(image_type) 
            cE.show_selected_images(images_roi, COLORS['Cyan'], 55, 15) # analyzes whole image_2_rois directory and write results

            # =============================================================================
            # Overwrite runtime.txt with next Phase
            # =============================================================================  
            with open("runtime.txt") as f:
                lines = f.readlines()
                lines[0] = "Phase: 3\n"
            with open("runtime.txt", "w") as f:
                f.writelines(lines)   
        
        # =================================
        # PHASE 3:
        # Image Moving
        # =================================
        elif lines[0] == "Phase: 3\n":
            print("__________________________________")
            print("\nMoving Images...")
            print("__________________________________")
            # ===================================================
            #  Move ROIs and Camera Image into timestamp folder
            # ===================================================
            from directoryHandling import fillDirRoi, fillDirCam, DirCAM, resetRuntimeTxt

            _, _, IMAGE_DIRECTORY_CAM, images_cam = DirCAM() # read directory state and take first image if present

            with open("runtime.txt") as f:
                lines = f.readlines()
            target_dir = lines[1][16:]

            fillDirRoi(target_dir) # move roi images into directory
            fillDirCam(IMAGE_DIRECTORY_CAM, target_dir) # move camera image into directory
            
            print("\n=================================================")
            print("\nTask completed...")
            print("\n=================================================")

            # =============================================================================
            # reset runtime.txt
            # =============================================================================  
            resetRuntimeTxt()

        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Oh no... something happend concerning the runtime.txt file")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    except IndexError:
        print("---------------------------------------------")
        print("\nSorry but there are no pictures in here...\nTrying again in 60s ...")
        print("---------------------------------------------") 
        time.sleep(60)
        #os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run 
        cycle()

    except KeyboardInterrupt:
        print("---------------------------------------------")
        print("\nTask stopped by user...")
        print("---------------------------------------------")
          
if __name__ == '__main__':
    cycle()
    pass

