# ==========================================================================================================================================================#
#                                                   main.py - handles script execution
# ==========================================================================================================================================================#

# =============================================================================
# Imports
# =============================================================================
import os
import sys
import time

from run import Pause, Restart

ROOT_DIR = os.path.abspath("../") # get parent directory

# =============================================================================
# run()
# =============================================================================

def run():

    try:

        print("Starting in 10s...")
        time.sleep(10)
        with open("runtime.txt") as f:
            lines = f.readlines()
        #print(lines)
        
        # =================================
        # PHASE 0: 
        # Creating Directory
        # =================================
        if lines[0] == "Phase: 0\n":

            print("\nInitializing script...\n")
            # =============================================================================
            # Check image_1_camera directory for images
            # =============================================================================
            import directoryHandling as dH
            image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = dH.DirCAM() # read directory state and take first image if present

            # =============================================================================
            # Create results file into timestamp directory
            # =============================================================================      
            print("Creating directory...")
            dH.createDir() # directory with current time

            # =============================================================================
            # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
            # =============================================================================      
            _, target_dir, text_file_location = dH.setupDir()

            dH.appendText("\nRESULT:\n", text_file_location)

            with open("runtime.txt") as f:
                lines = f.readlines()
                lines[0] = "Phase: 1\n"
                lines[1] = "Directory Path: "+target_dir
            with open("runtime.txt", "w") as f:
                f.writelines(lines)    

            raise Pause("Preparing next step...")

        # =================================
        # PHASE 1:
        # Object Detection
        # =================================            
        elif lines[0] == "Phase: 1\n":
            
            print("\nInitializing Object Detection...\n")
            # =============================================================================
            # Get first image in image_1_camera directory for the object detection
            # =============================================================================
            from directoryHandling import DirCAM
            image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = DirCAM() # read directory state and take first image if present

            # =================================
            #  Run first Dataset
            # =================================
            import MRCNN_Balloon as mrb
            mrb.MRCNN_Balloon(IMAGE_DIRECTORY_CAM, images_cam)

            # =============================================================================
            # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
            # =============================================================================  
            with open("runtime.txt") as f:
                lines = f.readlines()
                lines[0] = "Phase: 2\n"
            with open("runtime.txt", "w") as f:
                f.writelines(lines)    

            raise Pause("Preparing next step...")

        # =================================
        # PHASE 2:
        # Color Extraction
        # =================================            
        elif lines[0] == "Phase: 2\n":

            print("\nInitializing Color Analysis...\n")
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
            # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
            # =============================================================================  
            with open("runtime.txt") as f:
                lines = f.readlines()
                lines[0] = "Phase: 3\n"
            with open("runtime.txt", "w") as f:
                f.writelines(lines)    

            raise Pause("Preparing next step...")
        
        # =================================
        # PHASE 3:
        # Image Moving
        # =================================
        elif lines[0] == "Phase: 3\n":

            print("\nMoving Images...\n")
            # ===================================================
            #  Move ROIs and Camera Image into timestamp folder
            # ===================================================
            from directoryHandling import fillDirRoi, fillDirCam
            from directoryHandling import DirCAM
            image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = DirCAM() # read directory state and take first image if present

            with open("runtime.txt") as f:
                lines = f.readlines()
            target_dir = lines[1][16:]

            fillDirRoi(target_dir) # move roi images into directory
            fillDirCam(IMAGE_DIRECTORY_CAM, target_dir) # move camera image into directory
            
            print("\nTask completed...")

            # =============================================================================
            # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
            # =============================================================================  
            with open("runtime.txt") as f:
                lines = f.readlines()
                lines[0] = "Phase: 0\n"
                lines[1] = "Directory Path: "
            with open("runtime.txt", "w") as f:
                f.writelines(lines)    

        else:
            print("Oh no... something happend concerning the runtime.txt file")
    
    except Pause:
        print("\nContinuing in 15s ...")
        time.sleep(5)
        os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run
    
    except KeyboardInterrupt:
        print("\nTask stopped by user...")

        

# =============================================================================
# main
# =============================================================================           
if __name__ == '__main__':

    while True:

        try:
            
            print("Starting in 10s...")
            time.sleep(10)
            with open("runtime.txt") as f:
                lines = f.readlines()
            #print(lines)
            
        # =================================
        # PHASE 0:
        # Creating Directory
        # =================================
            if lines[0] == "Phase: 0\n":

                print("\nInitializing script...\n")
                # =============================================================================
                # Check image_1_camera directory for images
                # =============================================================================
                import directoryHandling as dH
                image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = dH.DirCAM() # read directory state and take first image if present

                # =============================================================================
                # Create results file into timestamp directory
                # =============================================================================      
                print("Creating directory...")
                dH.createDir() # directory with current time

                # =============================================================================
                # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
                # =============================================================================      
                _, target_dir, text_file_location = dH.setupDir()

                dH.appendText("\nRESULT:\n", text_file_location)

                with open("runtime.txt") as f:
                    lines = f.readlines()
                    lines[0] = "Phase: 1\n"
                    lines[1] = "Directory Path: "+target_dir
                with open("runtime.txt", "w") as f:
                    f.writelines(lines)    

                raise Pause("Preparing next step...")

        # =================================
        # PHASE 1:
        # Object Detection
        # =================================            
            elif lines[0] == "Phase: 1\n":
                
                print("\nInitializing Object Detection...\n")
                # =============================================================================
                # Get first image in image_1_camera directory for the object detection
                # =============================================================================
                from directoryHandling import DirCAM
                image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = DirCAM() # read directory state and take first image if present

                # =================================
                #  Run first Dataset
                # =================================
                import MRCNN_Balloon as mrb
                mrb.MRCNN_Balloon(IMAGE_DIRECTORY_CAM, images_cam)

                # =============================================================================
                # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
                # =============================================================================  
                with open("runtime.txt") as f:
                    lines = f.readlines()
                    lines[0] = "Phase: 2\n"
                with open("runtime.txt", "w") as f:
                    f.writelines(lines)    

                raise Pause("Preparing next step...")

        # =================================
        # PHASE 2:
        # Color Extraction
        # =================================            
            elif lines[0] == "Phase: 2\n":

                print("\nInitializing Color Analysis...\n")
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
                # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
                # =============================================================================  
                with open("runtime.txt") as f:
                    lines = f.readlines()
                    lines[0] = "Phase: 3\n"
                with open("runtime.txt", "w") as f:
                    f.writelines(lines)    

                raise Pause("Preparing next step...")
            

        # =================================
        # PHASE 3:
        # Image Moving
        # =================================
            elif lines[0] == "Phase: 3\n":

                print("\nMoving Images...\n")
                # ===================================================
                #  Move ROIs and Camera Image into timestamp folder
                # ===================================================
                from directoryHandling import fillDirRoi, fillDirCam
                from directoryHandling import DirCAM
                image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = DirCAM() # read directory state and take first image if present

                with open("runtime.txt") as f:
                    lines = f.readlines()
                target_dir = lines[1][16:]

                fillDirRoi(target_dir) # move roi images into directory
                fillDirCam(IMAGE_DIRECTORY_CAM, target_dir) # move camera image into directory
                
                print("\nTask completed...")

                # =============================================================================
                # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
                # =============================================================================  
                with open("runtime.txt") as f:
                    lines = f.readlines()
                    lines[0] = "Phase: 0\n"
                    lines[1] = "Directory Path: "
                with open("runtime.txt", "w") as f:
                    f.writelines(lines)    

                raise Restart

            else:
                print("Oh no... something happend concerning the runtime.txt file")
        
        # =============================================================================
        # handle exceptions and completly restart script
        # =============================================================================
        except IndexError:
            print("\nSorry but there are no pictures in here...\nTrying again in 30s ...")
            time.sleep(20)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run 

        except Pause:
            print("\nContinuing in 15s ...")
            time.sleep(5)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run

        except Restart:
            print("\nRestarting in 15s ...")
            time.sleep(5)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run               

        except KeyboardInterrupt:
            print("\nTask stopped by user...")

        else:
            print("Something happend....")
            break

