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

        print("\n=================================================")
        print("\nReading current Phase State\nPlease wait 10s...")
        print("\n=================================================")
        time.sleep(10)
        with open("runtime.txt") as f:
            lines = f.readlines()
        #print(lines)
        
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
            image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = dH.DirCAM() # read directory state and take first image if present

            # =============================================================================
            # Create results file into timestamp directory
            # ============================================================================= 
            print("__________________________________")   
            print("\nCreating directory...")
            print("__________________________________")
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

            raise Pause

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

            raise Pause

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
            # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
            # =============================================================================  
            with open("runtime.txt") as f:
                lines = f.readlines()
                lines[0] = "Phase: 3\n"
            with open("runtime.txt", "w") as f:
                f.writelines(lines)    

            raise Pause
        
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
            from directoryHandling import fillDirRoi, fillDirCam
            from directoryHandling import DirCAM
            image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = DirCAM() # read directory state and take first image if present

            with open("runtime.txt") as f:
                lines = f.readlines()
            target_dir = lines[1][16:]

            fillDirRoi(target_dir) # move roi images into directory
            fillDirCam(IMAGE_DIRECTORY_CAM, target_dir) # move camera image into directory
            
            print("\n=================================================")
            print("\nTask completed...")
            print("\n=================================================")

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
        print("---------------------------------------------")
        print("\nInitializing next Phase...\nReady in 15s...")
        print("---------------------------------------------")
        time.sleep(5)
        os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run
    
    except KeyboardInterrupt:
        print("---------------------------------------------")
        print("\nTask stopped by user...")
        print("---------------------------------------------")

        

# =============================================================================
# main
# =============================================================================           
if __name__ == '__main__':

    while True:

        try:
            
            print("\n=================================================")
            print("\nReading current Phase State\nPlease wait 10s...")
            print("\n=================================================")
            time.sleep(10)
            with open("runtime.txt") as f:
                lines = f.readlines()
            #print(lines)
            
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
                image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = dH.DirCAM() # read directory state and take first image if present

                # =============================================================================
                # Create results file into timestamp directory
                # =============================================================================      
                print("__________________________________")     
                print("\nCreating directory...")
                print("__________________________________")
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

                raise Pause

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

                raise Pause

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
                # Create new runtime.txt with next Phase and Timestamp Directory name and raise Pause
                # =============================================================================  
                with open("runtime.txt") as f:
                    lines = f.readlines()
                    lines[0] = "Phase: 3\n"
                with open("runtime.txt", "w") as f:
                    f.writelines(lines)    

                raise Pause
            

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
                from directoryHandling import fillDirRoi, fillDirCam
                from directoryHandling import DirCAM
                image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = DirCAM() # read directory state and take first image if present

                with open("runtime.txt") as f:
                    lines = f.readlines()
                target_dir = lines[1][16:]

                fillDirRoi(target_dir) # move roi images into directory
                fillDirCam(IMAGE_DIRECTORY_CAM, target_dir) # move camera image into directory
                
                print("\n=================================================")
                print("\nTask completed...")
                print("\n=================================================")

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
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Oh no... something happend concerning the runtime.txt file")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
        # =============================================================================
        # handle exceptions and completly restart script
        # =============================================================================
        except IndexError:
            print("---------------------------------------------")
            print("\nSorry but there are no pictures in here...\nTrying again in 30s ...")
            print("---------------------------------------------")
            time.sleep(20)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run 

        except Pause:
            print("---------------------------------------------")
            print("\nContinuing in 15s ...")
            print("---------------------------------------------")
            time.sleep(5)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run

        except Restart:
            print("---------------------------------------------")
            print("\nRestarting in 15s ...")
            print("---------------------------------------------")
            time.sleep(5)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run               

        except KeyboardInterrupt:
            print("---------------------------------------------")
            print("\nTask stopped by user...")
            print("---------------------------------------------")

        else:
            print("---------------------------------------------")
            print("Something happend....")
            print("---------------------------------------------")
            break

