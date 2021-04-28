import cv2
import numpy as np


img = cv2.imread('E:/Python/images/vue2.jpg')
img = cv2.resize(img, (512, 300))

_, thValue1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, thValue2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

# print(thValue1)
cv2.imshow('image', img)
cv2.imshow('thresholdImage1', thValue1)
cv2.imshow('thresholdImage2', thValue2)

cv2.waitKey(0)
cv2.destroyAllWindows()



