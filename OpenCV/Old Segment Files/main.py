import cv2
import numpy as np
import matplotlib.pyplot as plt
import all_segmentation
from all_segmentation import line_partitions
from all_segmentation import segmentation

inputImage = 'F:/Final year project/Test Images/Light.jpg'

camScanner = cv2.imread(inputImage)
name = plt.imshow(camScanner)
plt.title("Input Image")
plt.show()

grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 127, 255, cv2.THRESH_BINARY)

#############################################################################################################

# segmenting linesl.
segmentation(GaussianThresh5, 1)
line_array = all_segmentation.line_partitions

original = plt.imshow(camScanner)
plt.title("Input Image")
# plt.show()



number = int(input("Enter the line number : "))
string = "Line Number - " + str(number)
first_line = line_array[number-1]
plt.imshow(first_line)
plt.title(string)
plt.show()
# cv2.imshow("first_line", first_line)
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
