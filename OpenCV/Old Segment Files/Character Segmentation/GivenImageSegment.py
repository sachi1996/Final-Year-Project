import cv2
import numpy as np
from LineBreak import line_segment
from WordBreak import word_segment
from LineSegment import line_images
from LineSegment import word_images

line_partitions = [1,2,3]
start_points = [1,2,4]
end_points = [3,4,5]

def segmentation(Thresh_Image, axis_value):

    final_Image = Thresh_Image.copy();

    height, width = Thresh_Image.shape

    Thresh_Image[Thresh_Image == 0] = 1
    Thresh_Image[Thresh_Image == 255] = 0

    horizontal_projection = np.sum(Thresh_Image, axis=axis_value)

    row_index = 0;
    start_list = []
    end_list = []

    limit = 0
    if(axis_value == 1):
        line_segment(horizontal_projection, row_index, height, start_list, end_list);
        line_images(final_Image, start_list, end_list, height, width, limit)

    if(axis_value == 0):
        word_segment(start_list, end_list)
        word_images(final_Image, start_list, end_list, height, width, limit)





