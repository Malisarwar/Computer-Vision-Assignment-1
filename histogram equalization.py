# import Opencv
import cv2

# import Numpy
import numpy as np

# read a image using imread
img = cv2.imread(\'./images/01.jpg', 0)
img2 = cv2.imread(\'./images/02.jpg', 0)
img3 = cv2.imread(\'./images/05.jpg', 0)

# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)
equ2 = cv2.equalizeHist(img2)
equ3 = cv2.equalizeHist(img3)
# stacking images side-by-side
res = np.hstack((img, equ))
res2 = np.hstack((img2, equ))
res3 = np.hstack((img3, equ))
# show image input vs output
cv2.imshow(img)
cv2.imshow(img2)
cv2.imshow(img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
