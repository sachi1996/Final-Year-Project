import cv2
import matplotlib.pyplot as plt
import skimage.io as io
import numpy as np

Img_Original = io.imread('E:/img.png')


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

    # for i in range(len(horizontalZones)):
    #     name = "zone_" + str(i+1)
    #     name = plt.imshow(horizontalZones[i])
    #     plt.show()

    return horizontalZones


def projection(image):
    grayCamScanner = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
    _, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 170, 255, cv2.THRESH_BINARY)

    height, width = GaussianThresh5.shape

    GaussianThresh5[GaussianThresh5 == 0] = 1
    GaussianThresh5[GaussianThresh5 == 255] = 0

    horizontal_projection = np.sum(GaussianThresh5, axis=1)
    # print("\nProjections of zone")
    # print(horizontal_projection)
    return horizontal_projection


# calculate the number of black pixels
def blackPixelSum(horizontalProjection):
    count = 0
    for i in horizontalProjection:
        count += i
    print("Summation off black pixels : ", count)
    print("pixel density : ", (count/128))


zoneImages = []
zoneImages = zoneAreas(Img_Original)
print("\nlenght of zone", len(zoneImages), "\n")

index = 1
for i in zoneImages:
    if index == 16:
        break
    else:
        name = "- - - zone-number : " + str(index) + " - - -"
        print("\n\n",name)
        projections = projection(zoneImages[index])
        blackPixelCount = blackPixelSum(projections)
        # name = plt.imshow(zoneImages[6])
        # plt.show()
        index += 1
