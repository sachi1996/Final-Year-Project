import matplotlib.pyplot as plt
import cv2
import os

from numpy import vectorize


def chaincode(img):
    direction1 = 0
    direction2 = 0
    direction3 = 0
    direction4 = 0
    direction5 = 0
    direction6 = 0
    direction7 = 0
    direction8 = 0

    for i in range(1, 126):
        for j in range(1, 126):
            if img[i][j] == 1:
                if (img[i-1][j] == 1 and img[i-1][j+1] == 1 and img[i][j+1] and img[i+1][j+1]
                        and img[i+1][j] and img[i+1][j-1] and img[i][j - 1] == 1 and img[i-1][j-1] == 1):
                    break
                else:
                    if img[i-1][j] == 1:
                        direction1 += 1
                    if img[i-1][j+1] == 1:
                        direction2 += 1
                    if img[i][j+1] == 1:
                        direction3 += 1
                    if img[i+1][j+1] == 1:
                        direction4 += 1
                    if img[i+1][j] == 1:
                        direction5 += 1
                    if img[i+1][j-1] == 1:
                        direction6 += 1
                    if img[i][j-1] == 1:
                        direction7 += 1
                    if img[i-1][j-1] == 1:
                        direction8 += 1

    return direction1, direction2, direction3, direction4, direction5, direction6, direction7, direction8


input_image = cv2.imread("F:/SpellReaders/Datasets/By Class Dataset/by_class/79-y/hsf_1/hsf_1_00007.png")
grayCamScanner = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 170, 255, cv2.THRESH_BINARY)

GaussianThresh5[GaussianThresh5 == 0] = 1
GaussianThresh5[GaussianThresh5 == 255] = 0

d1, d2, d3, d4, d5, d6, d7, d8 = chaincode(GaussianThresh5)
total = d1 + d2 + d3 + d4 + d5 + + d6 + d7 + d8
percentage = 100 / total


Vector = []
Vector.append(d1 * percentage)
Vector.append(d2 * percentage)
Vector.append(d3 * percentage)
Vector.append(d4 * percentage)
Vector.append(d5 * percentage)
Vector.append(d6 * percentage)
Vector.append(d7 * percentage)
Vector.append(d8 * percentage)


BigTestChainCode = []
BigTestChainCode.append(Vector)


print(BigTestChainCode)
