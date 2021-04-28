import numpy as np

import cv2

img = cv2.imread('E:/Python/images/vue2.jpg')
me = cv2.imread('E:/Python/images/Me.jpg')

print(img.shape)
print(img.size)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# ROI
vue = img[280:340, 330:390]
img[273:333, 100:160] = vue

# Resize Images
img = cv2.resize(img, (512, 512))
me = cv2.resize(me, (512, 512))

# Add two images
combination = cv2.add(img, me)

# Add weight for images
combination = cv2.addWeighted(img, .2, me, .8, 0)

cv2.imshow('image', combination)

cv2.waitKey(0)
cv2.destroyAllWindows()

