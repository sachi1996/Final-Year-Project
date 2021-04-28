import cv2
import matplotlib.pyplot as plt
import numpy as np
import os




k = "E:/SpellReaders/Datasets/By Class Dataset/by_class/6b-k/hsf_1/hsf_1_00005.png"


def drawZoneLines(Img_Original):
    points = [32,64,96]
    for i in range(len(points)):
        h = cv2.line(Img_Original, (points[i], 0), (points[i], 128), (0, 255, 0), 1)
        v = cv2.line(h, (0, points[i]), (128, points[i]), (0,255,0), 1)
    return Img_Original


def zoneAreas(image):
    # get the zone values
    numberOfZones = 4
    zoneValues = []
    for i in range(0,numberOfZones+1):
        value = int(128/numberOfZones)*i
        zoneValues.append(value)

    # vertically cuts
    verticalZones = []
    vcount = 1
    for i in range(len(zoneValues)):
        if i == 4:
            break
        else:
            verticalZones.append(image[0:128, zoneValues[i]:zoneValues[vcount]])
            vcount += 1

    v_1 = verticalZones[0]
    v_2 = verticalZones[1]
    v_3 = verticalZones[2]
    v_4 = verticalZones[3]


    # horizontally cuts
    horizontalZones = []
    hcount = 1
    for i in range(len(zoneValues)):
        if i == 4:
            break
        else:
            horizontalZones.append(v_1[zoneValues[i]:zoneValues[hcount], 0:32])
            horizontalZones.append(v_2[zoneValues[i]:zoneValues[hcount], 0:32])
            horizontalZones.append(v_3[zoneValues[i]:zoneValues[hcount], 0:32])
            horizontalZones.append(v_4[zoneValues[i]:zoneValues[hcount], 0:32])
            hcount += 1

    return horizontalZones


def left_distance(height, width, image):
    left_distances = []
    for i in range(0, height):
        count = 0
        for j in range(0, width):
            if image[i][j] == 0:
                count += 1
                if count < 32:
                    pass
                if count == 32:
                    left_distances.append(0)
                    break
            if image[i][j] == 1:
                left_distances.append(j)
                break
            else:
                pass
    return left_distances


def upper_distance(height, width, image):
    upper_distances = []
    for i in range(0, width):
        count = 0
        for j in range(0, height):
            if image[j][i] == 0:
                count += 1
                if count < 32:
                    pass
                if count == 32:
                    upper_distances.append(0)
                    break
            if image[j][i] == 1:
                upper_distances.append(j)
                break
            else:
                pass
    return upper_distances


def img_threshold(input_image):
    grayCamScanner = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
    _, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 170, 255, cv2.THRESH_BINARY)

    GaussianThresh5[GaussianThresh5 == 0] = 1
    GaussianThresh5[GaussianThresh5 == 255] = 0

    return GaussianThresh5


def read_image_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)

    return images


dir = "E:/SpellReaders/Datasets/By Class Dataset/by_class/6d-m/hsf_1"
folderImges = read_image_folder(dir)
BigArray = []


character_z = "E:/SpellReaders/Datasets/By Class Dataset/by_class/5a-Z/hsf_1/hsf_1_00006.png"
image_Z = cv2.imread(character_z)
# img = cv2.imread(k)
zoneImages = img_threshold(image_Z)

for i in range(len(zoneImages)):
    Vector = []
    left = left_distance(32, 32, zoneImages[i])
    upper = upper_distance(32, 32, zoneImages[i])
    Vector.append(left)
    Vector.append(upper)
    BigArray.append(Vector)

print(BigArray)

divideImg = drawZoneLines(image_Z)
name = plt.imshow(divideImg)
plt.title("divide Image")
plt.show()


