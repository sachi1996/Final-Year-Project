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
