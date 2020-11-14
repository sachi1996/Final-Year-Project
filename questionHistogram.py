import cv2
import numpy as np

def projection(question_slices):
    for i in range(0, len(question_slices)):
        question_Image = question_slices[i];
        question_Image[question_Image == 0] = 1
        question_Image[question_Image == 255] = 0
        horizontally = np.sum(question_Image, axis=1)
        print(horizontally)
        return horizontally

