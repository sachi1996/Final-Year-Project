import cv2
import numpy as np

def segmentingLoop(horizontal_projection, row_index, limit, start_list, end_list):
        for pixel_count in horizontal_projection:
        #print(row_index + 1, pixel_count)
        if(pixel_count == 0):
            if(row_index < (limit - 1)):
                if((horizontal_projection[row_index - 1] == 0) and (horizontal_projection[row_index + 1] != 0)):
                    start_list.append(row_index + 1)
                if((horizontal_projection[row_index - 1] != 0) and (horizontal_projection[row_index + 1] == 0)):
                    end_list.append(row_index + 1)
                else:
                    pass
            else:
                pass
        else:
            pass

        row_index = row_index + 1

