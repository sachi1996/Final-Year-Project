import cv2
import numpy as np
from GivenImageSegment import segmentation

camScanner = cv2.imread('F:/Final year project/Test Images/28.jpg')
grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)
GaussianFiltered = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, binarizedImage = cv2.threshold(GaussianFiltered, 127, 255, cv2.THRESH_BINARY)

# segmenting lines
segmentation(binarizedImage, 1)

cv2.waitKey(0)
cv2.destroyAllWindows()

