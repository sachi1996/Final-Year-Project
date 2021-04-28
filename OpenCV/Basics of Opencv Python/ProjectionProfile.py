import cv2
import numpy as np
from matplotlib import pyplot as plt


camScanner = cv2.imread('E:/Final year project/Test Images/09.jpg' '')

# grayscale image
grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)

# Filtering
camScannerBlur = cv2.GaussianBlur(grayCamScanner, (5,5), 0)

# global threshold
_, thValue1 = cv2.threshold(camScannerBlur, 127, 255, cv2.THRESH_BINARY)
resizeImage = cv2.resize(thValue1, (900, 500))
cv2.imshow('simple with gaussian camScanner - 02', resizeImage)

# create blank image
blankImage = np.zeros((500, 900, 3), np.uint8)
cv2.imshow('blank image', blankImage)

# invert

resizeImage = 255 - resizeImage

# get projection
projection = np.sum(resizeImage,1)
print(projection)

# draw line for each rows in image
for row in range(resizeImage.shape[0]):
    cv2.line(blankImage, (0,row), (int(projection[row]*900/500),row), (255,255,255), 1)

cv2.imshow('result', blankImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
