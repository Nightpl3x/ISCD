# ==========================================================================================================================================================#
#                                                   colorExtraction.py 
#                             file for analysing images from the image_2_rois directory looking for a certain color
# ==========================================================================================================================================================#
# State: working
# TODO: need to check for optimal color for 'images' and maybe code clean up

# ==========================================================================
# Imports
# ==========================================================================
import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from collections import Counter
from sklearn.cluster import KMeans
from skimage.color import rgb2lab, deltaE_cie76

# ==========================================================================
# Main
# ==========================================================================
def RGB2HEX(color):
    yield "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_colors(image, number_of_colors, show_chart):
    
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
    
    counts = Counter(labels)
    # sort to ensure correct color percentage
    counts = dict(sorted(counts.items())) 
    
    center_colors = clf.cluster_centers_
    # get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if (show_chart):
        plt.figure(figsize = (8, 6))
        plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
        plt.show()

    yield rgb_colors

def match_image_by_color(image, color, threshold, number_of_colors ): 
    
    image_colors = get_colors(image, number_of_colors, False)
    selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

    select_image = False
    for i in range(number_of_colors):
        curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
        diff = deltaE_cie76(selected_color, curr_color)
        if (diff < threshold):
            select_image = True
    
    yield select_image

def show_selected_images(images, color, threshold, colors_to_match):

    import directoryHandling as dH
    from MRCNN_Balloon import image_type
    IMAGE_DIRECTORY_ROI, images_roi = dH.DirROI(image_type)

    for i in range(len(images)):
        
        selected = match_image_by_color(images[i],
                                        color,
                                        threshold,
                                        colors_to_match)
        if (selected):
            # ============================
            # Get and Print Image Name
            # ============================
            with Image.open(IMAGE_DIRECTORY_ROI[i]) as img:
                print("Sample: {}\n Result: POSITIVE\n" .format(img.filename))
            
            # append text to txt file
            dH.appendText("\nSample: {}\n Result: POSITIVE\n" .format(img.filename))

            # ============================
            # Output Exposed Image
            # ============================
            #images[i] = cv2.cvtColor(images[i],cv2.COLOR_BGR2RGB) # convert again to RGB Color Model because OpenCV uses BGR as Default Model
            #cv2.imshow("Exposed Sample: ",images[i])
            #cv2.waitKey(0)

        else:
            # ============================
            # Get and Print Image Name
            # ============================
            with Image.open(IMAGE_DIRECTORY_ROI[i]) as img:
                print("Sample: {}\n Result: NEGATIVE\n" .format(img.filename))

            # append text to txt file
            dH.appendText("\nSample: {}\n Result: NEGATIVE\n" .format(img.filename))

            
if __name__ == '__main__':
    print ("\nRunning colorExraction.py ...")
else:
    print ("\nImporting colorExraction.py ...")