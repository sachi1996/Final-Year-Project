import cv2
import matplotlib.pyplot as plt
import skimage.io as io
import numpy as np
import os

character_z = "E:/SpellReaders/Datasets/By Class Dataset/by_class/5a-Z/hsf_1/hsf_1_00006.png"
character_k = "E:/SpellReaders/Datasets/By Class Dataset/by_class/6b/hsf_1/hsf_1_00005.png"

"""
image_z = cv2.imread(character_z)
name = plt.imshow(image_z)
plt.title("Character - Z")
plt.show()
"""
Img_Original = cv2.imread(character_z)
FeatureVector = []


def drawZoneLines(Img_Original):
    points = [32,64,96]
    for i in range(len(points)):
        h = cv2.line(Img_Original, (points[i], 0), (points[i], 128), (0, 255, 0), 1)
        v = cv2.line(h, (0, points[i]), (128, points[i]), (0,255,0), 1)
    return Img_Original


def read_image_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)

    return images


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


def projection(image):
    grayCamScanner = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
    _, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 170, 255, cv2.THRESH_BINARY)

    GaussianThresh5[GaussianThresh5 == 0] = 1
    GaussianThresh5[GaussianThresh5 == 255] = 0

    horizontal_projection = np.sum(GaussianThresh5, axis=1)
    return horizontal_projection


def blackPixelSum(horizontalProjection):  # calculate the sum of black pixels
    count = 0
    for i in horizontalProjection:
        count += i
    density = (count/(32*32))*100
    # print("Pixel Density : ", round(density, 3))
    FeatureVector.append(round(density, 3))


###############################################################################################
# Change to read image folder - -- >

# m - 4d/hsf_0
# z - 5a-Z/hsf_0, hsf_1
# dir = "E:/SpellReaders/Datasets/By Class Dataset/by_class/5a-Z/hsf_1"
# dir = "E:/SpellReaders/Datasets/By Class Dataset/by_class/6d-m/hsf_1"
dir = "F:/SpellReaders/Datasets/By Class Dataset/by_class/4b-K/hsf_1"

BigZoneDensity = []

folderImges = read_image_folder(dir)
for t in range(len(folderImges)):
    zoneImages = zoneAreas(folderImges[t])
    index = 0
    FeatureVector = []
    for i in range(len(zoneImages)):
        projections = projection(zoneImages[index])
        blackPixelSum(projections)
        index += 1

    # print("\nimage : " + str(t))
    # print(FeatureVector)
    BigZoneDensity.append(FeatureVector)

print("\n\n")

print(BigZoneDensity)
#####################################################################################################

