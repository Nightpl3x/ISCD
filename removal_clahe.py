
import cv2
import numpy as np
import variables as v

img = v.image_gray
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow("CLAHE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()