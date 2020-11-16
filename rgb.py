import matplotlib.pyplot as plt
import numpy as np
im = cv2.imread('./images/06.jpg')
plt.imshow(im)
plt.show()
im2 = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
plt.imshow(im2)
plt.show()
hsv_im = cv.cvtColor(im, cv2.COLOR_RGB2HSV)
hsv_im2 = cv.cvtColor(im2, cv2.COLOR_RGB2HSV)
