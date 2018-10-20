def read_from_file(filename):
    with open(filename) as file:
        lines = file.readlines()

    pairs = []
    for elem in lines[1:]:
        pairs.append(tuple(map(int, elem.split())))
    print("Entered pairs" + str(pairs)[1:-1])

    return pairs


def gorokhivskiy_wedding_algorithm(pairs):
    # algorithm for creating tribes with unique elements
    tribes = [[pairs[0][0], pairs[0][1]]]

    tribes[0].__len__()
    for i in range(1, pairs.__len__()):
        tribes_len = tribes.__len__()
        add_item = False
        for j in range(tribes_len):
            tribes_item_len = tribes[j].__len__()
            for k in range(tribes_item_len):
                if tribes[j][k] == pairs[i][0]:
                    tribes[j].append(pairs[i][1])
                    add_item = True
                    break
                elif tribes[j][k] == pairs[i][1]:
                    tribes[j].append(pairs[i][0])
                    add_item = True
                    break
        if not add_item:
            tribes.append([pairs[i][0], pairs[i][1]])

    print("All tribes: " + str(tribes))

    # algorithm for counting possible pairs
    wedding_count = 0
    wedd_pairs = []
    if tribes.__len__() > 1:
        for i in range(tribes.__len__() - 1):
            for j in range(tribes[i].__len__()):
                for i_next in range(i + 1, tribes.__len__()):
                    for j_next in range(tribes[i_next].__len__()):
                        if tribes[i][j] % 2 == 0 and tribes[i_next][j_next] % 2 != 0:
                            wedding_count += 1
                            wedd_pairs.append( (tribes[i][j], tribes[i_next][j_next]) )
                        elif tribes[i][j] % 2 != 0 and tribes[i_next][j_next] % 2 == 0:
                            wedding_count += 1
                            wedd_pairs.append((tribes[i][j], tribes[i_next][j_next]))
    print("All wedding pairs: " + str(wedd_pairs) + "\n")
    return wedding_count


# main function
pairs = read_from_file("in2")
wedd_count = gorokhivskiy_wedding_algorithm(pairs)
print("Total possible weddings: %d \n" % wedd_count)
