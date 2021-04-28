def word_segment(start_list, end_list):

    word_slices_start = []
    word_slices_end = []

    for t in range(0, len(start_list) - 1):
        if ((start_list[t + 1] - end_list[t]) > 35):
            word_slices_start.append(start_list[t + 1])
            word_slices_end.append(end_list[t])
        else:
            continue

    word_slices_end.append(end_list[-1])