import cv2
import os
import matplotlib.pyplot as plt


def read_image_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)

    for i in range(len(images)):
        Title = "Image-" + str(i+1)
        name = plt.imshow(images[i])
        plt.title(Title)
        plt.show()

    return images


dir = "E:/Characters"
read_image_folder(dir)

