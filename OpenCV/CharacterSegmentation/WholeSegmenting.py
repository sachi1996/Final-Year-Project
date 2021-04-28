import cv2
import matplotlib.pyplot as plt
import numpy as np
from LineSegmenting import projection_segment
from WordSegmenting import word_segment

inputImage = 'F:/Final year project/Test Images/Light.jpg'

BigChar = []
char_line = []
###########################################################################################
# Apply preProcessing for input image

camScanner = cv2.imread(inputImage)
grayCamScanner = cv2.cvtColor(camScanner, cv2.COLOR_BGR2GRAY)
GaussianFiltered5 = cv2.GaussianBlur(grayCamScanner, (5, 5), 0)
_, GaussianThresh5 = cv2.threshold(GaussianFiltered5, 127, 255, cv2.THRESH_BINARY)

original = GaussianThresh5.copy()

height, width = original.shape

original[original == 0] = 1
original[original == 255] = 0

horizontal_projection = np.sum(original, 1)


#######################################################################################################
# Apply line segmnentation

row_index = 0
line_start = []
line_end = []
word_start = []
word_end = []
char_start = []
char_end = []

projection_segment(horizontal_projection, row_index, height, line_start, line_end)

line_slices = []
word_slices = []
char_slices = []
for x in range(len(line_start)):
    line_slices.append(original[line_start[x]:line_end[x], 0:width])
    img1 = line_slices[x]
    line_height, line_width = img1.shape
    line_name = "Line - " + str(x + 1)
    plt.imshow(line_slices[x], cmap='gray')
    plt.title(line_name)
    plt.show()

    # vericle projection is taken
    verticle_projection = np.sum(img1, 0)
    char_start.clear()  # clear previous appended values
    char_end.clear() # clear previous appended values
    char_slices.clear() # clear previous appended values
    word_start.clear() # clear previous appended values
    word_end.clear() # clear previous appended values
    word_slices.clear() # clear previous appended values
    projection_segment(verticle_projection, row_index, width, char_start, char_end) # char start and ends taken
    word_start = [char_start[0]]
    word_end = []
    word_segment(char_start, char_end, word_start, word_end) # word start and ends taken

    # append and show word slices
    for t in range(0, len(word_start)):
        word_slices.append(img1[0:line_height, word_start[t]:word_end[t]])
        name = "Word - " + str(t + 1)
        plt.imshow(word_slices[t], cmap='gray')
        plt.title(name)
        plt.show()

    # append and show character slices
    for t in range(0, len(char_start)):
        char_slices.append(img1[0:line_height, char_start[t]:char_end[t]])
        char_line.append(img1[0:line_height, char_start[t]:char_end[t]])
        char_name = "Char - " + str(t + 1)
        plt.imshow(char_slices[t], cmap='gray')
        plt.title(char_name)
        plt.show()

    BigChar.append(char_line)

cv2.waitKey(0)
cv2.destroyAllWindows()


