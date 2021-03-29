import cv2
import variables as v

img = v.image_copy
#img = cv2.resize(img, (800, 800))
cv2.normalize(img, None, 0, 255, cv2.NORM_L1)
cv2.imshow('dst_rt', img)
#cv2.imwrite('norm.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()