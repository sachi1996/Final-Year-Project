import cv2
from GivenImageSegment import segmentation

def line_images(final_Image, start_list, end_list, height, width, limit):

    line_slices = []
    for x in range(len(start_list)):
        line_slices.append(final_Image[start_list[x]:end_list[x], 0:width])
        name = "line_" + str(x + 1)
        cv2.imshow(name, line_slices[x])

    segmentation(line_slices[8], 0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def word_images(final_Image, start_list, end_list, height, width, limit):

    word_slices = []
    for t in range(0, len(start_list)):
        word_slices.append(final_Image[0:height, start_list[t]:end_list[t]])
        # name = "line_" + str(t + 1)
        # cv2.imshow(name, word_slices[t])

    cv2.waitKey(0)
    cv2.destroyAllWindows()