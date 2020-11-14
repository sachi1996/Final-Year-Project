import cv2
import numpy as np
from matplotlib import *
import all_segmentation
from all_segmentation import segmentation

camScanner = cv2.imread('E:/Final year project/Test Images/20.jpg')
grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)

# GaussianFiltered3 = cv2.GaussianBlur(grayCamScanner, (3, 3), 0)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)

# _, Gaussian3 = cv2.threshold(GaussianFiltered3, 170, 255, cv2.THRESH_BINARY)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 170, 255, cv2.THRESH_BINARY)

#############################################################################################################

# segmenting lines
segmentation(GaussianThresh5, 1)
line_array = []
line_array = all_segmentation.line_partitions

first_line = line_array[0]
cv2.imshow("first_line", first_line)
#############################################################################################################

# segmenting characters

# length = len(line_array)
# for i in range(0, length):
#     # line_image = "line_image_" + str(i)
#     # line_image = []
#     segmentation(line_array[i], 0)
#     character_array = []
#     character_array = line_segmentation.character_partitions

segmentation(first_line, 0)
# character_array = []
# character_array = line_segmentation.character_partitions
# character_image = character_array[4]
# cv2.imshow('character-image', character_image)

#############################################################################################################

cv2.waitKey(0)
cv2.destroyAllWindows()