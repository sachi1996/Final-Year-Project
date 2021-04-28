print(binarizedImage. shape)
height, width = binarizedImage.shape
print('width:  ', width)
print('height: ', height)

# Convert black spots to ones & white spots to zeros for binarized image
binarizedImage[binarizedImage == 0] = 1
binarizedImage[binarizedImage == 255] = 0


horizontal_projection = np.sum(binarizedImage, axis=1)
print(horizontal_projection)


# create blank image
blankImage = np.zeros((height, width, 3), np.uint8)

# draw line for each rows in image
for row in range(binarizedImage.shape[0]):
    cv2.line(blankImage, (0,row), (int(horizontal_projection[row]*width/height),row), (255,255,255), 1)

cv2.imshow('result', blankImage)