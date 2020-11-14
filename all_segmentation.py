import cv2
import numpy as np
from Word_segmentation import word
from segment_lines import line_segment
from questionHistogram import projection
from Question_segmentation import question

question_partitions = [1,1,1]
line_partitions = [1,2,3]
character_partitions = [4,5,6]
word_partitions = [7,8,9]

def segmentation(Thresh_Image, axis_value):

    final_Image = Thresh_Image.copy();

    height, width = Thresh_Image.shape

    Thresh_Image[Thresh_Image == 0] = 1
    Thresh_Image[Thresh_Image == 255] = 0

    horizontal_projection = np.sum(Thresh_Image, axis=axis_value)

############################################################################################################
# for loop for segmenting
    # segmentingLoop(horizontal_projection, row_index, limit, start_list, end_list)

    limit = 0
    if(axis_value == 1):
        limit = height
    if(axis_value == 0):
        limit = width

    row_index = 0;
    start_list = []
    end_list = []

    line_segment(horizontal_projection, row_index, limit, start_list, end_list)

#############################################################################################################
    # kadena images tika wena wenama array ekakata append karagaththa
    if axis_value == 1:

        print("\n- - - - - - - - - - - - - - - - - - - line cordinations > > > > > > > > ")
        print(start_list)
        print(end_list)

        # question_start = [start_list[0]]
        # question_end = []
        # question_slices = []
        #
        # question(start_list, end_list, question_start, question_end)

        # for x in range(len(question_start)):
        #     question_slices.append(final_Image[question_start[x]:question_end[x], 0:width])
        #     name = "Answer_" + str(x+1)
        #     cv2.imshow(name, question_slices[x])

        # tell which line and which question
        x = 0
        # for t in range(0, len(question_start)):
        #     for i in range(0, len(start_list)):
        #         line_slices.append(final_Image[start_list[i]:end_list[i], 0:width])
        #         if end_list[x] <= question_end[t]:
        #             current = "Answer_" + str(t+1) + "_line_" + str(i+1)
        #             # cv2.imshow(current, line_slices[x])
        #             x = x + 1
        #         if x == len(start_list):
        #             break;

        line_slices = []
        for x in range(len(start_list)):
                line_slices.append(final_Image[start_list[x]:end_list[x], 0:width])
                name = "line_" + str(x+1)
                # cv2.imshow(name, line_slices[x])

        global line_partitions
        line_partitions = line_slices

    if axis_value == 0:

        # character_slices = []
        # for i in range(0, len(start_list)):
        #     character_slices.append(final_Image[0:height, start_list[i]:end_list[i]])
        #     # name = "character_" + str(i)
        #     # cv2.imshow(name, character_slices[i])
        #
        # global character_partitions
        # character_partitions = character_slices

        word_start = [start_list[0]]
        word_end = []
        word(start_list, end_list, word_start, word_end)

        word_slices = []
        for t in range(0, len(word_start)):
            word_slices.append(final_Image[0:height, word_start[t]:word_end[t]])
        #
        # print(" / / / / / / / / / / / / / / / / / / / // / / / / / / / / / / / / / /")
        # projection(word_slices)

        # global word_partitions
        # word_partitions = word_slices

    ###############################################################################################################
