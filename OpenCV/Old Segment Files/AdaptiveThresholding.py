import cv2
import numpy as np

img1 = cv2.imread('E:/Python/Test Images/01.jpg', 0)
img2 = cv2.imread('E:/Python/Test Images/04.jpg', 0)
img1 = cv2.resize(img1, (512, 300))
img2 = cv2.resize(img2, (512, 300))

th_img1_mean = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th_img1_gaussian = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

th_img2_mean = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th_img2_gaussian = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('original', img1)
cv2.imshow('adaptive_thresh_mean_01', th_img1_mean)
cv2.imshow('adaptive_thresh_gaussian_01', th_img1_gaussian)
cv2.imshow('adaptive_thresh_mean_02', th_img2_mean)
cv2.imshow('adaptive_thresh_gaussian_02', th_img2_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()

