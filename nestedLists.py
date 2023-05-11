if __name__ == '__main__':
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        student_list.append([name, score])
        student_list.sort(key=lambda cell:(cell[1], cell[0]))

        lowest = second_lowest = student_list[0][1]
        value_update = 0
        i = 0
        size = len(student_list)

    while i < size:
        if student_list[i][1] > second_lowest:
            second_lowest = student_list[i][1]
            value_update += 1
        if value_update == 1:
            print(student_list[i][0])
        if lowest != second_lowest and value_update > 1:
            break
        i += 1



