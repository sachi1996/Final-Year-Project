import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


k = "E:/SpellReaders/Datasets/By Class Dataset/by_class/6b-k/hsf_1/hsf_1_00005.png"


def read_image_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)

    return images


Vector = []

def left_right_distance(height, width, image):
    left_min = width
    for i in range(0, height):
        for j in range(0, width):
            if image[i][j] == 1:
                if j < left_min:
                    left_min = j
                break
            else:
                pass

    right_min = width
    for i in range(0, height):
        for j in range(0, width):
            if image[i][127-j] == 1:
                if j < right_min:
                    right_min = j
                break
            else:
                pass
            j -= 1
    return left_min, right_min


def up_down_distance(height, width, image):
    up_min = height
    for i in range(0, width):
        for j in range(0, height):
            if image[j][i] == 1:
                if j < up_min:
                    up_min = j
                break
            else:
                pass

    down_min = height
    for i in range(0, width):
        for j in range(0, height):
            if image[127-j][i] == 1:
                if j < down_min:
                    down_min = j
                break
            else:
                pass
            j -= 1
    return up_min, down_min

"""
img = cv2.imread(k)
grayCamScanner = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 170, 255, cv2.THRESH_BINARY)

GaussianThresh5[GaussianThresh5 == 0] = 1
GaussianThresh5[GaussianThresh5 == 255] = 0

plt.imshow(GaussianThresh5)
plt.show()

l, r = left_right_distance(128, 128, GaussianThresh5)
u, d = up_down_distance(128, 128, GaussianThresh5)
Vector.append(l)
Vector.append(r)
Vector.append(u)
Vector.append(d)
print(Vector)

print("\nCharacter Width : ", (128 - r) - l)
print("Character Height : ", (128 - u) - d)
"""

#######################################################################################################
  # Applying to all images in a directory

# dir = "E:/SpellReaders/Datasets/By Class Dataset/by_class/5a-Z/hsf_1"
# dir = "E:/SpellReaders/Datasets/By Class Dataset/by_class/6d-m/hsf_1"
dir = "E:/SpellReaders/Datasets/By Class Dataset/by_class/4b-K/hsf_1"


images = read_image_folder(dir)

BigMinDistance = []
for i in range(len(images)):
    grayCamScanner = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
    _, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 170, 255, cv2.THRESH_BINARY)

    GaussianThresh5[GaussianThresh5 == 0] = 1
    GaussianThresh5[GaussianThresh5 == 255] = 0
    Vector = []
    l, r = left_right_distance(128, 128, GaussianThresh5)
    u, d = up_down_distance(128, 128, GaussianThresh5)
    Vector.append(l)
    Vector.append(r)
    Vector.append(u)
    Vector.append(d)
    BigMinDistance.append(Vector)






