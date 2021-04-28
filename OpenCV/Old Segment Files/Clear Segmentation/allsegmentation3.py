import cv2
import matplotlib.pyplot as plt
import numpy as np


inputImage = cv2.imread('E:/Final year project/Test Images/2244.jpg')


def projection(raw_image, axis_value):

    grayCamScanner = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
    GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
    _, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 127, 255, cv2.THRESH_BINARY)


    height, width = GaussianThresh5.shape

    GaussianThresh5[GaussianThresh5 == 0] = 1
    GaussianThresh5[GaussianThresh5 == 255] = 0

    h_v_projection = np.sum(GaussianThresh5, axis=axis_value)

    return height, width, h_v_projection


def segmentLWC(hgt_wdt, proj):
    start = []
    end = []
    row_index = 0
    for i in range(len(proj)):
        if proj[i] == 0:
            if row_index < (hgt_wdt - 1):
                if (proj[row_index - 1] == 0) and (proj[row_index + 1] != 0):
                    start.append(row_index + 1)
                if (proj[row_index - 1] != 0) and (proj[row_index + 1] == 0):
                    end.append(row_index + 1)
                else:
                    pass
            else:
                pass
        else:
            pass

        row_index = row_index + 1

    return start, end


height, width, projections = projection(inputImage, 1)
lineStart, lineEnd = segmentLWC(height, projections)


line1 = inputImage[lineStart[0]:lineEnd[0], 0:width]
plt.imshow(line1)
plt.show()


charStart, charEnd = segmentLWC(width, projections)

for i in range(len(charStart)):
    character = line1[0:height, charStart[i]:charEnd[i]]
    plt.imshow(character)
    plt.show()

