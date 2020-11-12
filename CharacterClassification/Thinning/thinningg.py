import cv2
import matplotlib
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
import skimage.io as io

"load image data"
Img_Original = io.imread('E:/Final year project/Test Images/10.jpg')

Otsu_Threshold = threshold_otsu(Img_Original)
BW_Original = Img_Original < Otsu_Threshold


def neighbours(x, y, image):
    img = image
    x_1, y_1, x1, y1 = x - 1, y - 1, x + 1, y + 1
    return [img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1],  # p2,p3,p4,p5
            img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1]]  # p6,p7,p8,p9


def transitions(neighbours):
    "No. of 0,1 patterns (transitions from 0 to 1) in the ordered sequence"
    n = neighbours + neighbours[0:1]  # p2, p3, ... , p8, p9, p2
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]))  # (p2,p3), (p3,p4), ... , (p8,p9), (p9,p2)


def zhangSuen(image):
    "the Zhang-Suen Thinning Algorithm"
    image_thinned = image.copy()  # deepcopy to protect the original image
    changing1 = changing2 = 1  # the points to be removed (set as 0)
    while changing1 or changing2:  # iterates until no further changes occur in the image
        # Step 1
        changing1 = []
        rows, columns = image_thinned.shape  # x for rows, y for columns
        for x in range(1, rows - 1):  # No. of  rows
            for y in range(1, columns - 1):  # No. of columns
                p2, p3, p4, p5, p6, p7, p8, p9 = n = neighbours(x, y, image_thinned)
                if (image_thinned[x][y] == 1 and  # Condition 0: Point P1 in the object regions
                        2 <= sum(n) <= 6 and  # Condition 1: 2<= N(P1) <= 6
                        transitions(n) == 1 and  # Condition 2: S(P1)=1
                        p2 * p4 * p6 == 0 and  # Condition 3
                        p4 * p6 * p8 == 0):  # Condition 4
                    changing1.append((x, y))
        for x, y in changing1:
            image_thinned[x][y] = 0
        # Step 2
        changing2 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                p2, p3, p4, p5, p6, p7, p8, p9 = n = neighbours(x, y, image_thinned)
                if (image_thinned[x][y] == 1 and  # Condition 0
                        2 <= sum(n) <= 6 and  # Condition 1
                        transitions(n) == 1 and  # Condition 2
                        p2 * p4 * p8 == 0 and  # Condition 3
                        p2 * p6 * p8 == 0):  # Condition 4
                    changing2.append((x, y))
        for x, y in changing2:
            image_thinned[x][y] = 0
    return image_thinned


"Apply the algorithm on images"
BW_Skeleton = zhangSuen(BW_Original)
# BW_Skeleton = BW_Original
"Display the results"
fig, ax = plt.subplots(1, 2)
ax1, ax2 = ax.ravel()
ax1.imshow(BW_Original, cmap=plt.cm.gray)
ax1.set_title('Original binary image')
ax1.axis('off')
ax2.imshow(BW_Skeleton, cmap=plt.cm.gray)
ax2.set_title('Skeleton of the image')
ax2.axis('off')
plt.show()

