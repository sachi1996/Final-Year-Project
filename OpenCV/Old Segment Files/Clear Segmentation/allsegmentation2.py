import cv2
import matplotlib.pyplot as plt
import numpy as np
from word_slices2 import word
from segmented_lines2 import line_segment

question_partitions = [1,1,1]
line_partitions = [1,2,3]
character_partitions = [4,5,6]
word_partitions = [7,8,9]

def segmentation(Thresh_Image, axis_value):

    final_Image = Thresh_Image.copy();

    height, width = Thresh_Image.shape

    Thresh_Image[Thresh_Image == 0] = 1
    Thresh_Image[Thresh_Image == 255] = 0

    h_v_projection = np.sum(Thresh_Image, axis=axis_value)

############################################################################################################
# for loop for segmenting
    # segmentingLoop(h_v_projection, row_index, limit, start_list, end_list)

    limit = 0
    if(axis_value == 1):
        limit = height
    if(axis_value == 0):
        limit = width

    row_index = 0;
    start_list = []
    end_list = []

    line_segment(h_v_projection, row_index, limit, start_list, end_list)

#############################################################################################################
    # kadena images tika wena wenama array ekakata append karagaththa
    if axis_value == 1:

        print("\n- - - - - - - - - - - - - - - - - - - line cordinations > > > > > > > > ")
        print(start_list)
        print(end_list)

        # question - - - -

        line_slices = []
        for x in range(len(start_list)):
                line_slices.append(final_Image[start_list[x]:end_list[x], 0:width])
                name = "line : " + str(x+1)
                Imgname = plt.imshow(line_slices[x])
                plt.title(name)
                plt.show()

        global line_partitions
        line_partitions = line_slices

    if axis_value == 0:

        word_start = [start_list[0]]
        word_end = []
        word(start_list, end_list, word_start, word_end)

        word_slices = []
        for t in range(0, len(word_start)):
            word_slices.append(final_Image[0:height, word_start[t]:word_end[t]])
            name = "Word - " + str(t+1)
            Imgname = plt.imshow(word_slices[t])
            plt.title(name)
            plt.show()

        character_slices = []
        for i in range(0, len(start_list)):
            character_slices.append(final_Image[0:height, start_list[i]:end_list[i]])
            charName = "character - " + str(i+1)
            # cv2.imshow(name, character_slices[i])
            name = plt.imshow(character_slices[i])
            plt.title(charName)
            plt.show()

        global character_partitions
        character_partitions = character_slices


        #
        # print(" / / / / / / / / / / / / / / / / / / / // / / / / / / / / / / / / / /")
        # projection(word_slices)

        # global word_partitions
        # word_partitions = word_slices

    ###############################################################################################################
