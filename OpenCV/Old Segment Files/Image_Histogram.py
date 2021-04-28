import cv2
import numpy as np
from matplotlib import pyplot as plt

camScanner = cv2.imread('E:/Final year project/Test Images/10.jpg' '')
grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)

# Filtering
GaussianFiltered = cv2.GaussianBlur(grayCamScanner, (5,5), 0)

# global threshold
_, binarizedImage = cv2.threshold(GaussianFiltered, 127, 255, cv2.THRESH_BINARY)
final_Image = binarizedImage.copy();

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

height, width = binarizedImage.shape
print('width:  ', width)
print('height: ', height)

binarizedImage[binarizedImage == 0] = 1
binarizedImage[binarizedImage == 255] = 0

horizontal_projection = np.sum(binarizedImage, axis=1)
print(horizontal_projection)

    # create blank image
blankImage = np.zeros((height, width, 3), np.uint8)

    # draw line for each rows in image
for row in range(binarizedImage.shape[0]):
    cv2.line(blankImage, (0, row), (int(horizontal_projection[row] * width / height), row), (255, 255, 255), 1)

cv2.imshow('result', blankImage);

################################################################################################################
row_index = 0;
start_row_list = []
end_row_list = []

for pixel_count in horizontal_projection:
    print(row_index + 1, pixel_count)
    if (pixel_count == 0):
        if (row_index < (height - 1)):
            if ((horizontal_projection[row_index - 1] == 0) and (horizontal_projection[row_index + 1] != 0)):
                start_row_list.append(row_index + 1)
            if ((horizontal_projection[row_index - 1] != 0) and (horizontal_projection[row_index + 1] == 0)):
                end_row_list.append(row_index + 1)
            else:
                pass
        else:
            pass
    else:
        pass

    row_index = row_index + 1;

print(start_row_list)
print(end_row_list)
print(len(start_row_list))

croppedImage1 = final_Image[start_row_list[0]:end_row_list[0], 0:width]

cv2.imshow("croppedImage1", croppedImage1)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# waitkeys of the image
cv2.waitKey(0)
cv2.destroyAllWindows()

# resizeImage = cv2.resize(thValue1, (900, 500))
# cv2.imshow('simple with gaussian camScanner - 02', resizeImage)


