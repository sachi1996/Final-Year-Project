def question(start_list, end_list, question_start, question_end):
    for t in range(0, len(start_list) - 1):
        if ((start_list[t + 1] - end_list[t]) > 60):
            question_start.append(start_list[t + 1])
            question_end.append(end_list[t])
        else:
            continue

    question_end.append(end_list[-1])

    print("Question Start and end coordinates - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(question_start)
    print(question_end)