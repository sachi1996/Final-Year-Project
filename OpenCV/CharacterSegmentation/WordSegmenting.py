def word_segment(start_list, end_list, word_start, word_end):
    for t in range(0, len(start_list) - 1):
        if (start_list[t + 1] - end_list[t]) > 22:
            word_start.append(start_list[t + 1])
            word_end.append(end_list[t])
        else:
            continue

    word_end.append(end_list[-1])

    print("\n- - - - - - - - - - word cordinations > > > > > > > > ")
    print(word_start)
    print(word_end)

