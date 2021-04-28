import cv2
import numpy as np
import matplotlib.pyplot as plt
import allsegmentation2
from allsegmentation3 import projection

camScanner = cv2.imread('E:/Final year project/Test Images/2244.jpg')
name = plt.imshow(camScanner)
plt.title("Input Image")
plt.show()
grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 127, 255, cv2.THRESH_BINARY)


projection(GaussianThresh5, 1)


cv2.waitKey(0)
cv2.destroyAllWindows()
