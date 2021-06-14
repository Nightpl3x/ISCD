# ==========================================================================================================================================================#
#                                                                       startup.py 
# ==========================================================================================================================================================#

if __name__ == '__main__':

    print ("\nRunning startup.py ...")

    # =============================================================================
    # Global Imports
    # =============================================================================
    import glob
    import cv2
    import utils as xct
    
    # =============================================================================
    # Directory of images to run detection on
    # =============================================================================
    IMAGE_DIRECTORY_CAM = glob.glob(xct.path_folder_cam+"/*.jpeg") # create list based on image names --> strings
    IMAGE_DIRECTORY_CAM.sort()         # sort list
    images_cam = [cv2.imread(img) for img in IMAGE_DIRECTORY_CAM] # create additional list for storing images --> ndarrays
    images_cam = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in images_cam] # convert from bgr back to rgb

    # =============================================================================
    # Check image_1_camera directory for images
    # =============================================================================
    if len(images_cam) == 0:
        print("\nSorry but there are no pictures in here...")

    elif len(images_cam) > 0:
        print("\nStarting process...\n")

        # =============================================================================
        # Import Datasets
        # =============================================================================        
        import Mask_RCNN_Coco as mrc
        import Mask_RCNN_Balloon as mrb

        # =============================================================================
        # Analyze one image at the time from camera dictionary
        # =============================================================================
        for index in range(len(images_cam)):

            # =============================================================================
            # Create directory with timestamp to move images into
            # =============================================================================
            import directoryHandling as dH
            dH.createDir() 

            # =================================
            #  Run first Dataset
            # =================================
            mrb.MRCNN_Balloon(IMAGE_DIRECTORY_CAM[index], images_cam[index])
            #mrc.MRCNN_Coco(IMAGE_DIRECTORY_CAM[index], images_cam[index]) # Test

            # ========================================
            #  Check if first dataset was successfull
            # ========================================
            IMAGE_DIRECTORY_ROI = glob.glob(xct.path_folder_roi+"/*.jpeg") # create list based on image names --> strings

            if len(IMAGE_DIRECTORY_ROI) == 0:
                mrc.MRCNN_Coco(IMAGE_DIRECTORY_CAM[index], images_cam[index])
                #mrb.MRCNN_Balloon(IMAGE_DIRECTORY_CAM[index], images_cam[index]) # Test

            # =================================
            #  Analyze ROIs
            # =================================
            print("\n")          
            import colorExtraction as cE 
            cE.show_selected_images(cE.images_roi, cE.COLORS['Cyan'], 55, 15, IMAGE_DIRECTORY_ROI[index]) # analyzes whole image_2_rois directory

            # =================================
            #  Move ROIs and Camera Image into timestamp folder
            # =================================
            dH.fillDirRoi() # move roi images into directory
            dH.fillDirCam(IMAGE_DIRECTORY_CAM[index]) # move camera image into directory

            print("\nExited task successfully...")


else:
    print ('\nImporting startup.py ...')
    
    