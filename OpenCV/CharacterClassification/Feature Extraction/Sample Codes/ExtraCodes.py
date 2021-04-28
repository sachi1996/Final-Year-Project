import cv2
import numpy as np


camScanner = cv2.imread(PhoneRuled)
grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 127, 255, cv2.THRESH_BINARY)

height, width = Thresh_Image.shape

Thresh_Image[Thresh_Image == 0] = 1
Thresh_Image[Thresh_Image == 255] = 0

horizontal_projection = np.sum(Thresh_Image, 1)
print(horizontal_projection)
    #
blankImage = np.zeros((height, width, 3), np.uint8)

for row in range(height):cv2.line(blankImage, (0, row), (int(horizontal_projection[row] * width / height), row), (255, 255, 255), 1)


project = 'E:/Final year project/Test Images/28.jpg'
report = 'E:/Final year project/Test Images/28828.jpg'
spellreaders = 'E:/Final year project/Test Images/2244.jpg' # done
PhoneHalfSheet = 'E:/Final year project/Test Images/Phone2.jpg' # done
Print = 'E:/Final year project/Test Images/8888.png' # done


# CSV writing new data
# # writing to csv file
# with open(filename, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
#
#     # writing the fields
#     csvwriter.writerow(fields)
#
#     # writing the data rows
#     csvwriter.writerows(rows)









# folderImages = read_image_folder("E:/Characters")
#
# for t in range(len(folderImages)):
#     FeatureVector = []
#     Img = folderImages[t]
#     zoneImages = zoneAreas(Img)
#     index = 0
#     for i in range(len(zoneImages)):
#         projections = projection(zoneImages[index])
#         blackPixelSum(projections)
#         index += 1
#     print("Image_" + str(t+1) + " : Feature Vector --->>>")
#     print(FeatureVector)
#     print("\n")
#     # greenImage = drawZoneLines(Img)
#     # plt.imshow(greenImage)
#     # plt.show()

################################################################################################################