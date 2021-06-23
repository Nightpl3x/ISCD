# ==========================================================================================================================================================#
#                                                   main.py - handles script execution
# ==========================================================================================================================================================#
def run():
    # =============================================================================
    # Check image_1_camera directory for images
    # =============================================================================
    import directoryHandling as dH

    image_cam_name, IMAGE_DIRECTORY_CAM, images_cam = dH.DirCAM() # read directory state and take first image if present

    if len(IMAGE_DIRECTORY_CAM) == 0:
        print("\nSorry but there are no pictures in here...")

    elif len(IMAGE_DIRECTORY_CAM) > 0:
        print("\nStarting process...\n")

        # =============================================================================
        # Create results file into timestamp directory
        # =============================================================================      
        dH.createDir() # directory with current time
        dH.appendText("\nRESULT:\n")

        # =================================
        #  Run first Dataset
        # =================================
        import MRCNN_Balloon as mrb
        
        mrb.MRCNN_Balloon(IMAGE_DIRECTORY_CAM, images_cam)

        # =================================
        #  Analyze ROIs
        # =================================
        from MRCNN_Balloon import image_type
        IMAGE_DIRECTORY_ROI, images_roi = dH.DirROI(image_type)
        print("\n")          
        import utils as xct
        import colorExtraction as cE 
        cE.show_selected_images(images_roi, xct.COLORS['Cyan'], 55, 15) # analyzes whole image_2_rois directory and write results

        # ===================================================
        #  Move ROIs and Camera Image into timestamp folder
        # ===================================================
        dH.fillDirRoi() # move roi images into directory
        dH.fillDirCam(IMAGE_DIRECTORY_CAM) # move camera image into directory
        
        print("\nTask completed...")

if __name__ == '__main__':
    print("Running main.py directly wont work")
else:
    print("\nImporting main.py...") 