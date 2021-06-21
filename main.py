# ==========================================================================================================================================================#
#                                                                   main.py 
# ==========================================================================================================================================================#

if __name__ == '__main__':

    print ("\nRunning main.py ...")

    # =============================================================================
    # Check image_1_camera directory for images
    # =============================================================================
    import utils as xct

    IMAGE_DIRECTORY_CAM_PREP = xct.DirCAM(dir)
    IMAGE_DIRECTORY_CAM = IMAGE_DIRECTORY_CAM_PREP[0]
    images_cam_prep = xct.DirCAM(dir)
    images_cam = images_cam_prep[1]

    if len(IMAGE_DIRECTORY_CAM) == 0:
        print("\nSorry but there are no pictures in here...")

    elif len(IMAGE_DIRECTORY_CAM) > 0:
        print("\nStarting process...\n")

        # =============================================================================
        # Import Datasets
        # =============================================================================        
        import MRCNN_Coco as mrc
        import MRCNN_Balloon as mrb

        # =============================================================================
        # Create directory with timestamp to move images into
        # =============================================================================
        import directoryHandling as dH
        dH.createDir()
        dH.createText("RESULTS:\n")

        # =============================================================================
        # Analyze one image at the time from camera dictionary
        # =============================================================================
        for index in range(len(IMAGE_DIRECTORY_CAM)):

            # =================================
            #  Run first Dataset
            # =================================
            mrb.MRCNN_Balloon(IMAGE_DIRECTORY_CAM[index], images_cam[index])

            # ========================================
            #  Check if first dataset was successfull
            # ========================================
            IMAGE_DIRECTORY_ROI_PREP = xct.DirROI(dir)
            IMAGE_DIRECTORY_ROI = IMAGE_DIRECTORY_ROI_PREP[0]
            images_roi_prep = xct.DirROI(dir)
            images_roi = images_roi_prep[1]

            if len(IMAGE_DIRECTORY_ROI) == 0:
                mrc.MRCNN_Coco(IMAGE_DIRECTORY_CAM[index], images_cam[index])

            # =================================
            #  Analyze ROIs
            # =================================
            print("\n")          
            import colorExtraction as cE 
            cE.show_selected_images(images_roi, xct.COLORS['Cyan'], 55, 15) # analyzes whole image_2_rois directory

            # =================================
            #  Move ROIs and Camera Image into timestamp folder
            # =================================
            dH.fillDirRoi() # move roi images into directory
            dH.fillDirCam(IMAGE_DIRECTORY_CAM[index]) # move camera image into directory

            print("\nTask complete...")


else:
    print ('\nImporting main.py ...')
    
    