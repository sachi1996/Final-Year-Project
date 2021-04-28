import cv2
from GivenImageSegment import segmentation

def word(line_slices, axis):

    segmentation(line_slices, 0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()