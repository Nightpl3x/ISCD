# ==========================================================================================================================================================#
#                                                                   main.py 
# ==========================================================================================================================================================#

def run():
    # =============================================================================
    # Check image_1_camera directory for images
    # =============================================================================
    import os 
    import skimage.io as io

    import directoryHandling as dH

    
    IMAGE_DIRECTORY_CAM, images_cam = dH.DirCAM("/*.jpeg") # read directory state

    if len(IMAGE_DIRECTORY_CAM) == 0:
        print("\nSorry but there are no pictures in here...")

    elif len(IMAGE_DIRECTORY_CAM) > 0:
        print("\nStarting process...\n")

        # =============================================================================
        # Get latest image
        # =============================================================================
        ROOT_DIR = os.path.abspath("../") # get parent directory
        path_folder_cam = os.listdir(ROOT_DIR+"/ColiChecker/images/image_1_camera")[0]
        image_cam_dir = ROOT_DIR+"/ColiChecker/images/image_1_camera/"+path_folder_cam
        image_cam = io.imread(ROOT_DIR+"/ColiChecker/images/image_1_camera/"+path_folder_cam)

        # =============================================================================
        # Create results file into timestamp directory
        # =============================================================================      
        dH.createDir() # directory with current time
        dH.appendText("\nRESULT:\n")

        # =================================
        #  Run first Dataset
        # =================================
        import MRCNN_Balloon as mrb
        mrb.MRCNN_Balloon(image_cam_dir, image_cam)

        # ========================================
        #  Check if first dataset was successfull
        # ========================================
        IMAGE_DIRECTORY_ROI, images_roi = dH.DirROI("/*.jpeg")
        '''
        if len(IMAGE_DIRECTORY_ROI) == 0:
            import MRCNN_Coco as mrc
            mrc.MRCNN_Coco(IMAGE_DIRECTORY_CAM[0], images_cam[0])
        '''
        # =================================
        #  Analyze ROIs
        # =================================
        print("\n")          
        import utils as xct
        import colorExtraction as cE 
        cE.show_selected_images(images_roi, xct.COLORS['Cyan'], 55, 15) # analyzes whole image_2_rois directory and write results

        # =================================
        #  Move ROIs and Camera Image into timestamp folder
        # =================================
        dH.fillDirRoi() # move roi images into directory
        dH.fillDirCam(image_cam_dir) # move camera image into directory
        
        print("\nTask completed...")

if __name__ == '__main__':
    print("Running main.py")
    run()
 
else:
    print("\nImporting main.py...")    
    