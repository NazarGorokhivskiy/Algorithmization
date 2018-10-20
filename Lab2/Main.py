LIST = [(1, 3)]


def gorokhivskiy_algorithm(list):
    left_index = 0
    right_index = 1
    list_size = list.__len__()

    # sorting list
    for n in range(1, list_size):
        indx = n - 1
        while (indx > -1) and list[indx + 1] < list[indx]:
            list[indx + 1], list[indx] = list[indx], list[indx + 1]
            indx -= 1

    # changing the list
    i = 0
    while i < list_size - 1:
        # conditions hell
        j = i + 1
        while j < list_size:
            if list[i][right_index] > list[j][right_index]:
                # list[i] "eats" list[j]
                list.pop(j)
                list_size -= 1
            else:
                # list[i][right] <= list[j][right]
                if list[i][right_index] < list[j][left_index]:
                    j += 1
                    continue
                else:
                    new_element = (list[i][left_index], list[j][right_index])
                    list[i] = new_element
                    list.pop(j)
                    list_size -= 1
        i += 1
    return list


print(gorokhivskiy_algorithm(LIST))