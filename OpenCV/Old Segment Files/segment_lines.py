def line_segment(projection, row_index, limit, start_list, end_list):
    for pixel_count in projection:
        # print(row_index + 1, pixel_count)
        if pixel_count == 0:
            if row_index < (limit - 1):
                if (projection[row_index - 1] == 0) and (projection[row_index + 1] != 0):
                    start_list.append(row_index + 1)
                if (projection[row_index - 1] != 0) and (projection[row_index + 1] == 0):
                    end_list.append(row_index + 1)
                else:
                    pass
            else:
                pass
        else:
            pass

        row_index = row_index + 1




