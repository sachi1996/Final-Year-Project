import cv2
import numpy as np
import matplotlib.pyplot as plt
import allsegmentation2
from allsegmentation2 import segmentation

camScanner = cv2.imread('E:/Final year project/Test Images/2244.jpg')
name = plt.imshow(camScanner)
plt.title("Input Image")
plt.show()
grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 127, 255, cv2.THRESH_BINARY)

#############################################################################################################

# segmenting lines
segmentation(GaussianThresh5, 1)
line_array = []
line_array = allsegmentation2.line_partitions
print(len(line_array))


original = plt.imshow(camScanner)
plt.title("Input Image")
plt.show()

number = int(input("Enter the line number : "))
string = "Line Number - " + str(number)
first_line = line_array[number-1]
name = plt.imshow(first_line)
plt.title(string)
plt.show()
# cv2.imshow("first_line", first_line)


#############################################################################################################

segmentation(first_line, 0)

#############################################################################################################

cv2.waitKey(0)
cv2.destroyAllWindows()
