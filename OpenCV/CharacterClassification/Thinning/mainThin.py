import cv2
import numpy as np
import zhang_zuen

img = cv2.imread('E:/SpellReaders/Datasets/By Class Dataset/by_class/6b-k/hsf_1/hsf_1_00005.png', 0)
retval, orig_thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
bin_thresh = (orig_thresh == 0).astype(int)

# convert all ones (black pixels) to zeroes, and all zeroes (white pixels) to ones
thresh = (zhang_zuen.thinned_thresh == 0).astype(np.uint8)
# convert ones to 255 (white)
thresh *= 255

# Resize the image
orig_threshR = cv2.resize(img, (500, 700))
threshR = cv2.resize(thresh, (500, 700))
# display original and thinned images
cv2.imshow('original image', orig_threshR)
cv2.imshow('thinned image', threshR)
cv2.waitKey(0)
cv2.destroyAllWindows()

