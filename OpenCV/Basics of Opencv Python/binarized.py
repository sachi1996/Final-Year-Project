import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("E:/Final year project/Test Images/2244.jpg")
cv2.imshow("image", image)

grayCamScanner = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("E:/Final year project/Test Images/saved.jpg", GaussianThresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()
