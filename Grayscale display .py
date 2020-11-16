from matplotlib import pyplot as plt
import cv2

img = cv2.imread('./images/08.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray)
plt.title('08 img')
plt.show()