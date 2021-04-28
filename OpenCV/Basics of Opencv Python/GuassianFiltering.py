import cv2
from PIL import Image

testImage = Image.open('E:/Final year project/Test Images/10.jpg')

width, height = testImage.size
  
# Setting the points for cropped image 
left = 5
top = height / 4
right = 164
bottom = 3 * height / 4
  
testImage.show()

croppedImage = testImage.crop((left, top, right, bottom))
croppedImage.show()

cv2.waitKey(0)
cv2.destroyAllWindows()