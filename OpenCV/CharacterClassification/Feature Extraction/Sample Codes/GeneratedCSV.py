import csv
# from zoning import BigZoneDensity
# from MinDistanceFeatures import BigMinDistance
from csv import writer

# print(len(BigZoneDensity))
# print(len(BigMinDistance))


arr1 = [[1,2], [3,4], [5,6]]
arr2 = [["a","b","c","d"], ["e","f","g","h"], ["i","j","k","l"]]
arr3 = [[11,22,33,44,55], [55,66,77,88,99], [111,222,333,444,555]]

BigArr = []

print(len(arr2[0]))

for i in range(3):
    arr = arr1[i]
    for j in range(4):
        arr.append(arr2[i][j])
    for k in range(5):
        arr.append(arr3[i][k])
    BigArr.append(arr)

print(BigArr)

