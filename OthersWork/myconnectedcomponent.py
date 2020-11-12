import cv2
import numpy as np
import matplotlib.pyplot as plt

camScanner = cv2.imread('E:/88.jpg')
grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 170, 255, cv2.THRESH_BINARY)


height, width = GaussianThresh5.shape

GaussianThresh5[GaussianThresh5 == 0] = 1
GaussianThresh5[GaussianThresh5 == 255] = 0


horizontal_projection = np.sum(GaussianThresh5, axis=1)
print(height)

for i in GaussianThresh5:
    print(GaussianThresh5[i])

plt.imshow(GaussianThresh5)
plt.axis("on")
plt.title("Orginal Image")
plt.show()

start_list =[]
end_list =[]

# for pixel_count in horizontal_projection:
#     # print(row_index + 1, pixel_count)
#     if pixel_count == 0:
#         if row_index < (height - 1):
#             if (horizontal_projection[row_index - 1] == 0) and (horizontal_projection[row_index + 1] != 0):
#                 start_list.append(row_index + 1)
#             if (horizontal_projection[row_index - 1] != 0) and (horizontal_projection[row_index + 1] == 0):
#                 end_list.append(row_index + 1)
#             else:
#                 pass
#         else:
#             pass
#     else:
#         pass
#
#     row_index = row_index + 1

cv2.waitKey(0)
cv2.destroyAllWindows()