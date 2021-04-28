import cv2
import numpy as np


# print(cv2.__version__)

image = cv2.imread('E:/Python/vue2.jpg', -1)  # Here you can give the path and label.

cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()



