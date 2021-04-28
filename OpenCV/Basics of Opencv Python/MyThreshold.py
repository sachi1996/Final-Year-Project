import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('E:/Final year project/Test Images/01.jpg', 0)
img = cv2.resize(img, (512, 300))

_, thValue1 = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)

# th_img1_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, c
# v2.THRESH_BINARY, 11, 2)
# mine = cv2.adaptiveThreshold(img, 210, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# cv2.imshow('original', img)
# cv2.imshow('binary', th_img1_mean)
# cv2.imshow('mine', mine)
cv2.imshow('simple', thValue1)

plt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

